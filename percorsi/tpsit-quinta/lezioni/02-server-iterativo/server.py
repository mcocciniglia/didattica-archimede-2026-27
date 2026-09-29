import socket


HOST = "127.0.0.1"
PORT = 50000


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((HOST, PORT))
        server.listen(1)

        print(f"Server in ascolto su {HOST}:{PORT}")

        while True:
            conn, addr = server.accept()

            print("Client connesso:", addr)

            with conn:
                while True:
                    dati = conn.recv(1024)

                    if not dati:
                        break

                    messaggio = dati.decode().strip()
                    print("Ricevuto:", messaggio)

                    risposta = "Hai scritto: " + messaggio
                    conn.sendall((risposta + "\n").encode())

            print("Client disconnesso")


if __name__ == "__main__":
    main()
