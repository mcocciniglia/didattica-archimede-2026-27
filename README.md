# Didattica Archimede 2026/27

Sito statico per i percorsi di laboratorio di Tecnologie informatiche,
TPSIT e Informatica dell'Istituto Archimede.

L'`index.html` nella radice è il portale generale e raccoglie percorsi
distinti per classe e disciplina: non rappresenta un corso sequenziale che
ogni studente debba seguire interamente.

La struttura iniziale comprende cinque percorsi:

- Tecnologie informatiche — classi prime;
- TPSIT — classe terza;
- TPSIT — classe quarta;
- TPSIT — classe quinta;
- Informatica — classe quinta.

## Stato

Sono disponibili le roadmap, gli indici dei percorsi, i template editoriali,
la pagina dei componenti e l'infrastruttura grafica. Le singole lezioni non
sono ancora state sviluppate.

## Consultazione locale

Aprire `index.html` con un browser moderno. Il progetto non richiede build,
installazione di pacchetti o servizi esterni.

## Architettura di accesso

- la homepage principale è l'indice generale dei percorsi dell'anno
  scolastico 2026/27;
- la pagina del singolo percorso è il normale punto di accesso degli studenti
  della classe e della disciplina corrispondenti.

## Struttura

```text
assets/                  stile e comportamento condivisi
docs/                    catalogo dei componenti
percorsi/                cinque indici didattici
roadmap/                 cinque roadmap in Markdown
_template-lezione/       modello per le lezioni future
_template-esercitazione/ modello per le attività future
fonti/                   fonti locali escluse da Git
index.html               homepage generale
404.html                 pagina non trovata
```

## Regole operative

Prima di modificare il progetto leggere `AGENTS.md`, `PROGETTO.md` e la
roadmap interessata. Tutti i collegamenti interni devono essere relativi e le
pagine devono usare `assets/archimede.css`.

## Riservatezza e pubblicazione

Il sito pubblico deve contenere soltanto materiali consultabili. Consegne,
feedback, valutazioni, soluzioni riservate e dati degli studenti appartengono
agli ambienti autenticati previsti dal progetto.

In questa fase non è configurato alcun repository remoto e non è stata
eseguita alcuna pubblicazione.
