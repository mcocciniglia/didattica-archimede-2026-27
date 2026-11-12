import socket


def leggi_riga(sock, buffer):
    while b"\n" not in buffer:
        dati = sock.recv(1024)
        if dati == b"":
            raise ConnectionError(
                "Connessione chiusa prima della risposta completa"
            )
        buffer += dati
    riga, buffer = buffer.split(b"\n", 1)
    return riga.decode("utf-8"), buffer


if __name__ == "__main__":
    with socket.create_connection(("127.0.0.1", 50000), timeout=5) as sock:
        buffer = b""
        for richiesta in ["PING", "ECHO ciao", "SALUTA"]:
            sock.sendall((richiesta + "\n").encode("utf-8"))
            risposta, buffer = leggi_riga(sock, buffer)
            print(repr(risposta))
