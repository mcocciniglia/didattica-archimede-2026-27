import socket


INDIRIZZO = ("127.0.0.1", 50000)


def leggi_riga(sock, buffer=b""):
    while b"\n" not in buffer:
        dati = sock.recv(1024)
        if dati == b"":
            raise ConnectionError("Connessione chiusa prima della risposta")
        buffer += dati
    riga, buffer = buffer.split(b"\n", 1)
    return riga.decode("utf-8")


with socket.create_connection(INDIRIZZO, timeout=3) as client_a:
    client_a.sendall(b"PING")
    print("A: inviati 4 byte senza LF; attende il completamento della riga.")

    with socket.create_connection(INDIRIZZO, timeout=3) as client_b:
        client_b.sendall(b"PING\n")
        print("B riceve:", leggi_riga(client_b))

    print("B ha ricevuto PONG mentre A era ancora senza risposta.")
    client_a.sendall(b"\n")
    print("A riceve dopo LF:", leggi_riga(client_a))