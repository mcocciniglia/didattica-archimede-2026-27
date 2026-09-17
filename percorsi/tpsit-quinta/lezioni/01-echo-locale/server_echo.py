import socket


HOST = "127.0.0.1"
PORT = 50000


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen(1)
        print(f"Server in ascolto su {HOST}:{PORT}")
        print("In attesa di un messaggio...")

        connection, address = server_socket.accept()
        with connection:
            print(f"Client collegato da {address[0]}")
            data = connection.recv(1024)
            message = data.decode("utf-8")
            print(f"Messaggio ricevuto: {message}")

            response = message
            connection.sendall(response.encode("utf-8"))
            print(f"Risposta inviata: {response}")

    print("Server terminato.")


if __name__ == "__main__":
    main()
