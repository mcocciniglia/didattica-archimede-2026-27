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
la pagina dei componenti e l'infrastruttura grafica. Le lezioni e i materiali
vengono sviluppati e pubblicati progressivamente durante l'anno scolastico.

## Consultazione locale

Aprire `index.html` con un browser moderno. Il progetto non richiede build o
installazione di pacchetti. Per caricare gli asset condivisi pubblicati da
`mcocciniglia/common` è necessaria una connessione di rete.

## Architettura di accesso

- la homepage principale è l'indice generale dei percorsi dell'anno
  scolastico 2026/27;
- la pagina del singolo percorso è il normale punto di accesso degli studenti
  della classe e della disciplina corrispondenti;
- ogni indice separa la **Roadmap / Moduli del percorso**, che descrive la
  progettazione complessiva, dai **Materiali disponibili / Lezioni**, che
  raccolgono soltanto le risorse effettivamente pubblicate;
- un eventuale riquadro **Stato del percorso** può comunicare l'avanzamento,
  senza sostituire l'elenco dei materiali disponibili.

## Struttura

```text
assets/                  stile e comportamento condivisi
docs/                    catalogo dei componenti
percorsi/                cinque indici didattici
roadmap/                 cinque roadmap in Markdown
_template-lezione/       modello comune per le lezioni
_template-esercitazione/ modello comune per le esercitazioni
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
agli ambienti autenticati previsti dal progetto, come Moodle o Google
Classroom secondo il percorso.

La pubblicazione del sito e le operazioni Git seguono la politica definita in
`AGENTS.md`; i contenuti pubblici sono destinati a GitHub Pages.
