# AGENTS.md

## Ambito del progetto

Questo repository contiene il sito didattico del Laboratorio di Informatica e
TPSIT dell'Istituto Archimede per l'anno scolastico 2026/27.

Il percorso di lavoro autorizzato è esclusivamente:

`C:\Github\didattica-archimede-2026-27`

Il repository `C:\Github\idoneita-terzo-anno` è una fonte esterna in sola
lettura: non deve mai essere modificato.

## Prima di intervenire

1. Verificare il percorso di lavoro.
2. Leggere `AGENTS.md`, `PROGETTO.md` e la roadmap del percorso coinvolto.
3. Consultare `docs/componenti.html` e i template pertinenti.
4. Controllare la coerenza con il percorso precedente e successivo.
5. Limitare la modifica ai file strettamente necessari.

## Fonti e autorità

- I materiali originali sono conservati in `fonti/`.
- `fonti/` è locale, esclusa da Git e non deve essere rinominata.
- Le roadmap Markdown sono la trascrizione editoriale delle fonti Word.
- In caso di dubbio sui contenuti didattici, prevale il documento Word del
  percorso interessato.
- Non inserire nelle pagine dati personali, credenziali, valutazioni o
  elaborati identificabili degli studenti.

## Struttura didattica

Il sito comprende cinque percorsi:

- Tecnologie informatiche — classi prime;
- TPSIT — classe terza;
- TPSIT — classe quarta;
- TPSIT — classe quinta;
- Informatica — classe quinta.

Ogni lezione o esercitazione futura deve stare in una cartella dedicata con
pagina principale `index.html`. Le lezioni e le esercitazioni devono rimanere
distinte. Non sviluppare una nuova lezione se non è stata richiesta
esplicitamente.

## Regole per HTML, CSS e JavaScript

- Usare HTML5 semantico e lingua italiana.
- Usare collegamenti interni relativi.
- Utilizzare il solo foglio `assets/archimede.css` per lo stile condiviso.
- Non aggiungere framework o dipendenze esterne senza autorizzazione.
- Mantenere JavaScript ridotto alle funzioni necessarie, come la preferenza di
  tema.
- Conservare la compatibilità con tema chiaro, tema scuro e stampa.
- Ogni pagina deve avere titolo, descrizione, skip link, navigazione coerente
  e gerarchia corretta delle intestazioni.

## Accessibilità

- Scrivere istruzioni brevi e sequenziali, adatte anche a studenti con DSA.
- Assicurare contrasto sufficiente, focus visibile e uso completo da tastiera.
- Non affidare un'informazione soltanto al colore.
- Fornire testo alternativo alle immagini informative.
- Usare tabelle soltanto per dati realmente tabellari, con intestazioni
  esplicite.
- Rispettare `prefers-reduced-motion`.

## Schema delle lezioni future

Ogni lezione deve includere almeno:

1. codice, titolo, durata e prerequisiti;
2. richiamo iniziale;
3. obiettivi osservabili;
4. esempio o dimostrazione;
5. attività guidata;
6. pratica autonoma o verifica;
7. evidenza/consegna attesa;
8. riepilogo e navigazione.

Ogni esercitazione deve dichiarare il percorso e la lezione di riferimento,
gli strumenti, i file iniziali, i criteri di completamento e gli aiuti
progressivi.

## Controlli finali

- Validare struttura HTML e percorsi relativi.
- Controllare tutti i collegamenti locali.
- Verificare leggibilità responsive, tema chiaro/scuro e stampa.
- Confrontare titoli, codici, ore e sequenza con la roadmap ufficiale.
- Verificare che `fonti/` continui a risultare ignorata da Git.
- Non eseguire push, pubblicazione, merge, creazione di remoti o modifiche al
  repository sorgente.

