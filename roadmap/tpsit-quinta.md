# TPSIT — classe quinta

Anno scolastico 2026/27 · 3 ore settimanali · scansione 2+1

## Scelta didattica

Un unico filo conduttore collega protocolli e architetture, servizi con i
socket e riuso degli stessi concetti in un'applicazione web e mobile.

## Monte ore

- circa 99 ore nominali;
- 87 ore pianificate;
- 6 ore di margine;
- 93 ore operative stimate.

Il blocco da 2 ore serve per costruire e collaudare; l'ora singola per
progettare, analizzare protocolli, correggere e verificare.

## Risultati attesi

Lo studente impara a:

- descrivere un'architettura applicativa di rete e motivare protocolli e porte;
- realizzare client e server TCP/UDP in Python, con errori, timeout e più client;
- progettare e documentare un protocollo applicativo;
- sviluppare un'applicazione web client/server con richieste sincrone e asincrone;
- produrre un client installabile come PWA e difendere il sistema realizzato.

## Roadmap annuale

| Periodo | Ore | Modulo | Attività | Evidenza |
| --- | ---: | --- | --- | --- |
| Settembre | 3 | M0 Avvio | Diagnostica Python/reti, ambiente, consegne e repository | Echo client/server |
| Settembre–ottobre | 15 | M1 Architetture | Livelli, TCP/IP, porte, client/server, TCP/UDP, traffico | Schema e analisi Wireshark |
| Novembre–gennaio | 27 | M2 Socket | TCP/UDP, protocollo, JSON, concorrenza, timeout, errori e test | Servizio multi-client |
| Febbraio | 6 | Pausa didattica | Diagnosi, laboratori graduati e micro-prova | Recupero documentato |
| Marzo | 9 | M3A Web | HTTP, routing, template, vista, logica e dati | Applicazione Flask minima |
| Marzo–aprile | 15 | M3B Servizi | API, JSON, fetch, validazione, errori, sessioni e sicurezza | Client e servizio integrati |
| Aprile | 6 | M3C Mobile | Manifest, responsive design, service worker e installazione | PWA installabile |
| Aprile–maggio | 6 | M3D Progetto | Integrazione, test, documentazione e demo | Prodotto e presentazione |
| Trasversale | 6 | Margine | Prove, orientamento, imprevisti e consolidamento | Tenuta del percorso |

## Ritmo settimanale

| Blocco | Funzione | Scansione |
| --- | --- | --- |
| 2 ore | Costruire e collaudare | 15 min richiamo; 30 dimostrazione; 60 laboratorio; 15 test e commit |
| 1 ora | Progettare e verificare | 10 min quiz; 20 protocollo/schema; 20 correzione; 10 diario |

Nell'ora singola si evitano attività con tempi di avvio elevati.

## Dettaglio dei moduli

### M0 — Ambiente e diagnostica · 3 ore

Prerequisiti TCP/IP e Python; ambiente virtuale; repository Git; primo
scambio di byte su localhost.

### M1 — Architetture di rete · 15 ore

Servizi e livelli; indirizzi, porte e socket; scelta TCP/UDP; DNS e HTTP;
cattura e interpretazione essenziale con Wireshark.

### M2 — Programmazione socket · 27 ore

Client/server TCP iterativo; server concorrente con threading; UDP;
framing, codifica, JSON, timeout, eccezioni; test e collaudo tra postazioni.

### Pausa didattica · 6 ore

Mappa degli errori, consegne differenziate su porte e socket, micro-prova con
seconda possibilità.

### M3 — Applicazioni web e mobile · 36 ore

HTTP e architettura web; Flask, routing, template, richieste e risposte;
separazione di interfaccia, logica e persistenza; API JSON e fetch; PWA
responsive; progetto integrato, test e demo.

## Stack didattico

| Uso | Strumento | Decisione |
| --- | --- | --- |
| Lezioni | Sito statico | Indice, spiegazioni, esempi e rubriche |
| Classe virtuale | Moodle | Consegne, quiz, feedback e file riservati |
| Sviluppo | VS Code e Python 3 | Ambiente leggero e virtual environment |
| Rete | socket e Wireshark | Meccanismo e osservazione degli scambi |
| Web server | Flask | Routing e ciclo richiesta/risposta visibili |
| Client | HTML, CSS e JavaScript | Fetch e DOM essenziali, niente framework obbligatorio |
| Test API | Bruno | Collezioni versionabili come file |
| Mobile | PWA | Prodotto installabile senza seconda toolchain |
| Progettazione | diagrams.net | Schemi leggibili ed esportabili |

## Coordinamento con Informatica

Informatica cura dati, SQL e applicazione PHP/MySQL; TPSIT cura
comunicazione, protocolli, servizi, distribuzione e client asincrono. Il
dominio applicativo può coincidere, ma repository, prove e criteri restano
distinti. La persistenza può essere JSON, SQLite o il database di Informatica.

## Valutazione

| Evidenza | Peso | Criteri |
| --- | ---: | --- |
| Architetture e protocolli | 15% | Lessico e scelta motivata |
| Prove socket | 30% | Funzionamento, errori, concorrenza e test |
| Applicazione web | 25% | Architettura, asincronia, codice e sicurezza |
| Progetto e difesa | 20% | Integrazione, documentazione e modifica individuale |
| Processo professionale | 10% | Consegne, commit, diario e revisione |

## Obiettivi minimi

- distinguere client/server, TCP/UDP, indirizzo/porta;
- realizzare client e server per un protocollo semplice;
- gestire almeno un errore di rete e un timeout;
- creare una pagina Flask dinamica con richiesta `fetch`;
- consegnare codice e istruzioni riproducibili.

## Progetto finale

Specifiche minime:

- server raggiungibile in rete locale e almeno un client web;
- tre operazioni con richieste e risposte JSON;
- gestione di input non valido, timeout ed errore del servizio;
- aggiornamento asincrono con `fetch`;
- manifest e installazione PWA;
- README, architettura, API/protocollo e piano di test.

Milestone: **C1 Architettura**, **C2 Protocollo**, **C3 percorso completo**,
**C4 Beta**, **C5 Rilascio**.

## Prime quattro settimane

1. Diagnostica, indirizzi, porte, Python ed echo localhost.
2. Servizi, protocolli, porte e prima osservazione Wireshark.
3. Componenti client/server e sequenza di connessione TCP.
4. Primo client e server TCP con messaggi codificati.

## Preparazione docente

Verificare Python, ambienti virtuali, firewall e rete; predisporre catture
Wireshark alternative, starter TCP/UDP/Flask/PWA, rubriche, policy per l'IA e
un piano offline con pacchetti e documentazione locali.

