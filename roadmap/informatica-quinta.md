# Informatica — classe quinta

Anno scolastico 2026/27 · 4 ore settimanali · due gruppi classe

## Scelta didattica

Le due quinte seguono lo stesso percorso con dataset e dominio applicativo
diversi. Competenze, prove e rubrica restano comuni, riducendo la copiatura
senza duplicare la preparazione docente.

## Monte ore

- 120 ore effettive stimate;
- 112 ore pianificate;
- 8 ore flessibili;
- ritmo consigliato: due incontri da 2 ore.

## Risultati attesi

Lo studente impara a:

- progettare una base dati da requisiti, E-R e schema relazionale in 3NF;
- creare e interrogare un database con SQL;
- realizzare un'applicazione dinamica con PHP e PDO;
- usare validazione, query preparate, password hash, sessioni e ruoli;
- documentare, testare e presentare un prodotto software.

## Roadmap annuale

| Periodo | Ore | Modulo | Attività | Evidenza |
| --- | ---: | --- | --- | --- |
| Settembre | 4 | M0 Avvio | Diagnostica SQL/web, ambiente, consegne e repository | Pagina PHP e script SQL |
| Settembre–ottobre | 14 | M1 Analisi dati | Requisiti, entità, associazioni, cardinalità e dizionario | Modello concettuale |
| Ottobre | 14 | M2 Modello relazionale | Traduzione, chiavi, vincoli, anomalie e normalizzazione | Schema in 3NF |
| Novembre–dicembre | 24 | M3 SQL fondamentale | DDL, DML, SELECT, filtri, funzioni, aggregazioni e join | Database e query |
| Gennaio–febbraio | 14 | M4 SQL evoluto | Subquery, viste, transazioni, indici e privilegi | Caso pratico motivato |
| Febbraio–aprile | 26 | M5 PHP + PDO | Form, HTTP, validazione, prepared statement, CRUD, sessioni e ruoli | CRUD sicuro |
| Aprile | 8 | M6 API e JSON | Endpoint, codici HTTP, JSON e fetch | Mini API documentata |
| Aprile–maggio | 8 | M7 Qualità e sicurezza | Test, logging, errori, backup e OWASP essenziale | Report di hardening |
| Maggio | 14 | M8 Capstone | Sviluppo, review, documentazione, demo e colloquio | Prodotto e pitch |
| Trasversale | 8 | Margine | Recupero, prove, orientamento e imprevisti | Riallineamento |

## Ritmo settimanale

| Blocco | Funzione | Scansione |
| --- | --- | --- |
| A · 2 ore | Modellare e capire | 15 min obiettivo; 30 dimostrazione; 60 pratica; 15 exit ticket |
| B · 2 ore | Costruire e verificare | 10 min briefing; 75 progetto; 20 test/review; 15 commit/diario |

Con orario 3+1 il blocco lungo è dedicato allo sviluppo; con 4 ore
consecutive si cambia attività dopo circa 100 minuti.

## Dettaglio dei moduli

### M0 — Ambiente e diagnostica · 4 ore

VS Code, PHP, MariaDB e DBeaver; query diagnostiche; pagina dinamica minima;
convenzioni di cartelle, nomi, README, consegne e commit.

### M1 — Progettazione concettuale · 14 ore

Analisi di requisiti ambigui, domande al committente, E-R, cardinalità,
identificatori, generalizzazioni utili, dizionario e vincoli non grafici.

### M2 — Progettazione logica · 14 ore

Mapping di entità e associazioni; dipendenze funzionali; anomalie;
normalizzazione fino alla 3NF con casi realistici.

### M3–M4 — SQL · 38 ore

DDL/DML riproducibile; filtri, join e aggregazioni; viste, transazioni,
indici, utenti e privilegi; NoSQL soltanto come confronto motivato.

### M5 — Applicazione web data-driven · 26 ore

Form, GET/POST, validazione, PDO, query preparate, CRUD, sessioni,
`password_hash`, `password_verify`, ruoli e separazione tra pagine/controller,
servizi e accesso dati.

### M6–M8 — Integrazione e prodotto · 30 ore

Endpoint JSON, test e casi limite, backup/ripristino, capstone,
documentazione, demo e difesa delle scelte.

## Stack didattico

| Uso | Strumento | Decisione |
| --- | --- | --- |
| Lezioni | Sito statico | Spiegazioni, esempi e rubriche pubbliche |
| Classe virtuale | Moodle | Consegne, feedback, valutazioni e riservati |
| Versionamento | Git e GitHub | Commit piccoli; privati studenti se sostenibili |
| Database | MariaDB | Un database/utente per gruppo o studente |
| Client SQL | DBeaver Community | Query, metadati, import/export e controllo diagrammi |
| Back-end | PHP 8.x e PDO | Connessioni, parametri, errori e transazioni espliciti |
| Front-end | HTML/CSS e JS essenziale | Form, tabelle, validazione e fetch |
| Modellazione | diagrams.net | E-R leggibili e indipendenti dal DBMS |

## Organizzazione delle due quinte

| Elemento | Quinta A | Quinta B |
| --- | --- | --- |
| Dominio capstone | Prenotazione di risorse scolastiche | Help desk e ticket |
| Dataset | Aule, laboratori, utenti, fasce e prenotazioni | Utenti, asset, ticket, priorità e interventi |
| Funzioni | Ricerca, prenotazione, annullamento e report | Apertura, presa in carico, storico, SLA e report |

Materiali e prove sono comuni. Il progetto può essere svolto a coppie, ma ogni
studente sostiene una difesa individuale e una modifica assegnata.

## Valutazione

| Evidenza | Peso | Criteri |
| --- | ---: | --- |
| Progettazione E-R e logica | 15% | Correttezza, vincoli e normalizzazione |
| Prove SQL | 30% | Correttezza, leggibilità, efficacia e autonomia |
| Applicazione PHP/PDO | 25% | Funzionalità, sicurezza, errori e struttura |
| Capstone e difesa | 25% | Integrazione, test, documentazione e contributo |
| Processo professionale | 5% | Consegne, commit, diario e revisione |

Rubrica: **4 Autonomo e motivato**, **3 Adeguato**, **2 Parziale**,
**1 Iniziale**.

## Obiettivi minimi

- produrre un E-R semplice e tradurlo in tabelle;
- scrivere DDL/DML e query con filtri, join e aggregazioni;
- realizzare un CRUD PDO con query preparate;
- gestire un login e distinguere autenticazione/autorizzazione;
- consegnare codice, script e documentazione riproducibile.

## Capstone — specifica minima

- almeno 5 entità, relazioni 1:N e una N:M;
- script di creazione/popolamento, vincoli e dati di test;
- almeno 8 query, incluse join, aggregazione e subquery o vista;
- CRUD su due risorse, ricerca, login e due ruoli;
- validazione server-side, query preparate, password hash ed errori sicuri;
- README, E-R, dizionario, piano di test e manuale utente.

Milestone: **C1 Requisiti**, **C2 Dati**, **C3 Vertical slice**,
**C4 Beta**, **C5 Release**.

## Prime quattro settimane

1. Setup DB/PHP e baseline individuale.
2. Requisiti, entità, attributi e prima bozza E-R.
3. Cardinalità, vincoli, peer review e dizionario.
4. Mapping, chiavi esterne e DDL v1.

## Preparazione docente

Verificare MariaDB e PHP; preparare database template e account limitati;
coordinare prove e terminologia con il docente teorico; definire una policy IA
trasparente; predisporre materiali, dump e istruzioni offline.

