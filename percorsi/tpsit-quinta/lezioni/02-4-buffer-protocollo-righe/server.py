import socket
import threading


def prepara_risposta(riga):
    if riga == "PING":
        return "PONG"
    if riga.startswith("ECHO ") and len(riga) > 5:
        return "OK " + riga[5:]
    return "ERR comando"


def gestisci_client(conn, addr):
    buffer = b""
    with conn:
        while True:
            dati = conn.recv(1024)
            if dati == b"":
                if buffer:
                    print("Richiesta incompleta da", addr)
                break

            buffer += dati
            while b"\n" in buffer:
                riga_bytes, buffer = buffer.split(b"\n", 1)
                riga = riga_bytes.decode("utf-8")
                risposta = prepara_risposta(riga)
                conn.sendall((risposta + "\n").encode("utf-8"))


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind(("127.0.0.1", 50000))
        server.listen()
        print("Server pronto su 127.0.0.1:50000")
        while True:
            conn, addr = server.accept()
            threading.Thread(
                target=gestisci_client, args=(conn, addr), daemon=True
            ).start()


if __name__ == "__main__":
    main()
