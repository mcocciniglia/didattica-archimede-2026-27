import socket
import time


INDIRIZZO = ("127.0.0.1", 50000)
TIMEOUT_SERVER = 5


def leggi_riga(sock):
    buffer = b""
    while b"\n" not in buffer:
        dati = sock.recv(1024)
        if dati == b"":
            raise ConnectionError("Connessione chiusa prima della risposta")
        buffer += dati
    riga, _residuo = buffer.split(b"\n", 1)
    return riga


def nuova_connessione():
    return socket.create_connection(INDIRIZZO, timeout=TIMEOUT_SERVER + 3)


with nuova_connessione() as client:
    client.sendall(b"PING\n")
    assert leggi_riga(client) == b"PONG"
print("OK: PING -> PONG")

with nuova_connessione() as client:
    testo = b"x" * 75
    client.sendall(b"ECHO " + testo + b"\n")
    assert leggi_riga(client) == b"OK " + testo
print("OK: riga di esattamente 80 byte accettata")

with nuova_connessione() as client:
    client.sendall(b"ECHO " + b"x" * 76 + b"\n")
    assert leggi_riga(client) == b"ERR riga troppo lunga"
    assert client.recv(1) == b""
print("OK: riga di 81 byte rifiutata e connessione chiusa")

with nuova_connessione() as client:
    client.sendall(b"x" * 81)
    assert leggi_riga(client) == b"ERR riga troppo lunga"
    assert client.recv(1) == b""
print("OK: residuo di 81 byte senza LF rifiutato")

with nuova_connessione() as client:
    riga = b"ECHO " + b"y" * 75 + b"\n"
    client.sendall(riga + riga)
    assert leggi_riga(client) == b"OK " + b"y" * 75
    assert leggi_riga(client) == b"OK " + b"y" * 75
print("OK: due righe da 80 byte nello stesso invio")

with nuova_connessione() as client:
    inizio = time.monotonic()
    client.sendall(b"PING")
    assert client.recv(1) == b""
    durata = time.monotonic() - inizio
    assert durata >= TIMEOUT_SERVER - 1
print(f"OK: timeout con riga incompleta dopo circa {durata:.1f} secondi")

with nuova_connessione() as client:
    client.sendall(b"PING\n")
    assert leggi_riga(client) == b"PONG"
    client.shutdown(socket.SHUT_WR)
    assert client.recv(1) == b""
print("OK: chiusura ordinaria dopo una richiesta completa")

print("Tutti i collaudi di rete sono superati.")