import socket


if __name__ == "__main__":
    with socket.create_connection(("127.0.0.1", 50000), timeout=5) as sock:
        sock.sendall(b"PING")
        sock.shutdown(socket.SHUT_WR)
        print(repr(sock.recv(1024)))
