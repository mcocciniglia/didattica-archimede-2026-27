def ricostruisci(blocchi):
    buffer = b""
    righe = []

    for dati in blocchi:
        buffer += dati
        while b"\n" in buffer:
            riga, buffer = buffer.split(b"\n", 1)
            righe.append(riga.decode("utf-8"))

    return righe, buffer


if __name__ == "__main__":
    blocchi = [b"PING\nE", b"CHO sole\nPI", b"NG\n"]
    righe, residuo = ricostruisci(blocchi)
    print(righe)
    print(residuo)
