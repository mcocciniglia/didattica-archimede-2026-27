from server import MAX_RIGA_BYTES, aggiungi_blocco


def verifica(condizione, descrizione):
    if not condizione:
        raise AssertionError(descrizione)
    print("OK:", descrizione)


righe, residuo, errore = aggiungi_blocco(b"", b"PING\n")
verifica((righe, residuo, errore) == ([b"PING"], b"", None), "PING completo")

riga_80 = b"x" * MAX_RIGA_BYTES
righe, residuo, errore = aggiungi_blocco(b"", riga_80 + b"\n")
verifica((righe, residuo, errore) == ([riga_80], b"", None), "80 byte prima di LF")

riga_81 = b"x" * (MAX_RIGA_BYTES + 1)
righe, residuo, errore = aggiungi_blocco(b"", riga_81 + b"\n")
verifica(errore == "riga troppo lunga", "81 byte prima di LF")

blocco_con_due_righe = riga_80 + b"\n" + riga_80 + b"\n"
righe, residuo, errore = aggiungi_blocco(b"", blocco_con_due_righe)
verifica(
    (len(righe), all(len(riga) == MAX_RIGA_BYTES for riga in righe), errore)
    == (2, True, None),
    "due righe valide nello stesso blocco, oltre 80 byte complessivi",
)

righe, residuo, errore = aggiungi_blocco(b"", riga_81)
verifica(
    (righe, residuo, errore) == ([], riga_81, "riga troppo lunga"),
    "residuo oltre il limite senza LF",
)

righe, residuo, errore = aggiungi_blocco(b"", b"PI")
verifica((righe, residuo, errore) == ([], b"PI", None), "primo frammento senza LF")
righe, residuo, errore = aggiungi_blocco(residuo, b"NG\n")
verifica((righe, residuo, errore) == ([b"PING"], b"", None), "completamento su blocco successivo")

print("Tutte le verifiche deterministiche sono superate.")