# TPSIT — classe terza

Anno scolastico 2026/27 · 1 ora settimanale · circa 30 ore nominali

## Obiettivo annuale

Leggere il sistema operativo come insieme di risorse osservabili e
controllabili. Lo studente usa una shell in modo consapevole, osserva processi
e risorse, spiega paginazione e scheduling, gestisce file e produce un breve
rapporto tecnico riproducibile.

## Monte ore

- 26 ore pianificate;
- 4 ore di margine;
- lezioni tipiche da 55 minuti.

## Roadmap annuale

| Periodo | Ore | Nucleo | Laboratorio | Prodotto osservabile |
| --- | ---: | --- | --- | --- |
| Settembre | 2 | Avvio e metodo | Ambienti, cartelle, Moodle e terminale | Scheda diagnostica |
| Ottobre | 4 | Codifica | Script di conversione, esadecimale, dimensione dati, parità/checksum | Script commentato |
| Novembre–dicembre | 7 | Shell e file system | Percorsi, wildcard, redirect, pipe, permessi, ricerca e filtri | Script di backup/inventario |
| Gennaio–febbraio | 6 | Processi e scheduling | Processi, padre/figlio, FCFS e Round Robin | Log e tabella dei tempi |
| Marzo | 4 | Memoria | Indirizzi, pagine/frame, FIFO/LRU, uso memoria | Simulatore e commento |
| Aprile | 3 | I/O e periferiche | Driver, buffer, stampa, dispositivi, porte e prestazioni | Mappa del percorso I/O |
| Maggio | 4 | Compito autentico | Informazioni di sistema, automazione e documentazione | Mini-audit tecnico |

## Sequenza della lezione

1. 5 minuti — problema iniziale o previsione;
2. 10 minuti — dimostrazione essenziale;
3. 30 minuti — attività guidata a difficoltà crescente;
4. 10 minuti — consegna e riflessione finale.

## Strumenti

| Strumento | Uso | Scelta operativa |
| --- | --- | --- |
| Linux preconfigurato | Shell, processi, permessi e file system | WSL 2 se disponibile, altrimenti VM predisposta |
| Visual Studio Code | Testo, shell e script | Profilo minimale, Python e Hex Editor |
| Python 3 | Misura e simulazione | Script brevi a scheletro, nessun framework |
| Moodle | Quiz, consegne, feedback e recupero | Una sezione per modulo |

## Valutazione

| Evidenza | Peso | Forma |
| --- | ---: | --- |
| Checkpoint 1 | 15% | Codifica e lettura esadecimale |
| Checkpoint 2 | 25% | Shell e file system |
| Checkpoint 3 | 25% | Processi e memoria |
| Compito finale | 35% | Mini-audit e spiegazione orale di 3–5 minuti |

La rubrica considera correttezza tecnica, autonomia, metodo e comprensione.
Con una sola ora settimanale non è previsto un progetto software lungo: il
filo conduttore è l'osservazione del sistema.

## Organizzazione dei materiali

Le lezioni usano codici `3.01`, `3.02` e successivi. Il sito contiene
materiali consultabili e dati anonimizzati; Moodle gestisce consegne,
valutazioni e file riservati.

## Prime quattro settimane

1. Tour del sito e di Moodle, accessi e struttura della consegna.
2. Terminale: posizione, elenco, creazione e spostamento di file.
3. Osservazione di un file di testo in esadecimale.
4. Dimensione dei dati e primo script guidato.

## Preparazione docente

- predisporre sito, Moodle e template di lezione;
- provare e congelare l'ambiente Linux;
- mantenere una configurazione minima e uniforme;
- verificare sempre l'eseguibilità dei materiali prima della pubblicazione.

