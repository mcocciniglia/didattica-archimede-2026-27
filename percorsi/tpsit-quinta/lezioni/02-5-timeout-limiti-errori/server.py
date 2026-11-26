import socket
import threading


HOST = "127.0.0.1"
PORTA = 50000
TIMEOUT_RICEZIONE = 5
MAX_RIGA_BYTES = 80


def prepara_risposta(riga):
    if riga == "PING":
        return "PONG"
    if riga.startswith("ECHO ") and len(riga) > 5:
        return "OK " + riga[5:]
    return "ERR comando"


def aggiungi_blocco(buffer, dati):
    """Aggiunge byte e controlla ogni riga e il residuo non terminato."""
    buffer += dati
    righe = []

    while b"\n" in buffer:
        riga_bytes, buffer = buffer.split(b"\n", 1)
        if len(riga_bytes) > MAX_RIGA_BYTES:
            return righe, buffer, "riga troppo lunga"
        righe.append(riga_bytes)

    # Il residuo è una riga ancora aperta e non deve crescere senza LF.
    if len(buffer) > MAX_RIGA_BYTES:
        return righe, buffer, "riga troppo lunga"

    return righe, buffer, None


def gestisci_client(conn, addr):
    buffer = b""
    try:
        with conn:
            # Questo socket è dedicato al client accettato, non al listener.
            conn.settimeout(TIMEOUT_RICEZIONE)
            print("Connessione aperta:", addr)

            while True:
                try:
                    dati = conn.recv(1024)
                except socket.timeout:
                    print(
                        "Timeout di ricezione dopo",
                        TIMEOUT_RICEZIONE,
                        "secondi:",
                        addr,
                    )
                    break

                if dati == b"":
                    if buffer:
                        print("Fine flusso con riga incompleta:", addr)
                    else:
                        print("Chiusura ordinaria del client:", addr)
                    break

                # Prima si applica il framing e il limite; si decodifica dopo.
                righe, buffer, errore = aggiungi_blocco(buffer, dati)

                # La lunghezza è stata controllata sui byte, prima del decode.
                for riga_bytes in righe:
                    try:
                        riga = riga_bytes.decode("utf-8")
                    except UnicodeDecodeError:
                        conn.sendall(b"ERR codifica\n")
                        print("Riga non UTF-8; connessione chiusa:", addr)
                        return

                    risposta = prepara_risposta(riga)
                    conn.sendall((risposta + "\n").encode("utf-8"))

                if errore:
                    # Riga troppo lunga: risposta prevista, poi chiusura.
                    conn.sendall(b"ERR riga troppo lunga\n")
                    print("Limite di 80 byte superato:", addr)
                    break
    except socket.timeout:
        print("Timeout del socket durante la gestione del client:", addr)
    except OSError as errore:
        print(
            "Errore socket per",
            addr,
            "-",
            type(errore).__name__,
            ":",
            errore,
        )


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((HOST, PORTA))
        server.listen()
        print(f"Server pronto su {HOST}:{PORTA}")
        while True:
            try:
                conn, addr = server.accept()
            except OSError as errore:
                print("Errore socket in accept():", errore)
                break

            threading.Thread(
                target=gestisci_client, args=(conn, addr), daemon=True
            ).start()


if __name__ == "__main__":
    main()