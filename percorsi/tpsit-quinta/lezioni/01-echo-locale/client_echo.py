import socket


HOST = "127.0.0.1"
PORT = 50000


def main():
    message = input("Messaggio da inviare: ").strip()
    if not message:
        print("Nessun messaggio da inviare.")
        return

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            print(f"Connessione al server {HOST}:{PORT}...")
            client_socket.connect((HOST, PORT))
            client_socket.sendall(message.encode("utf-8"))
            print(f"Messaggio inviato: {message}")

            data = client_socket.recv(1024)
    except ConnectionRefusedError:
        raise SystemExit(
            "Connessione rifiutata: avvia prima il server e riprova."
        )

    response = data.decode("utf-8")
    print(f"Risposta ricevuta: {response}")


if __name__ == "__main__":
    main()
