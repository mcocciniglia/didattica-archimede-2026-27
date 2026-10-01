# TPSIT — classe quarta

Anno scolastico 2026/27 · 2 ore settimanali · circa 60 ore nominali

## Obiettivo annuale

Trasformare un problema in un progetto documentato e verificarne il
comportamento concorrente.

Il progetto guida è una semplice applicazione per richieste o ticket di
laboratorio. Lo stesso caso viene raffinato durante l'anno: requisiti,
diagrammi UML, architettura a livelli, repository Git e componente
concorrente.

## Monte ore

- 54 ore pianificate;
- 6 ore di margine.

## Roadmap annuale

| Periodo | Ore | Nucleo | Laboratorio | Prodotto osservabile |
| --- | ---: | --- | --- | --- |
| Settembre | 2 | Avvio e primi thread | Programma, processo, esecuzione sequenziale e primo esperimento con `threading.Thread` | Due script Python eseguibili e osservazioni |
| Settembre–ottobre | 6 | Requisiti | Stakeholder, requisiti, user story, criteri e tracciabilità | Specifica v1 e matrice |
| Ottobre–novembre | 10 | UML essenziale | Casi d'uso, attività, classi, sequenza e stati | Dossier UML versionato |
| Dicembre–gennaio | 6 | Ciclo di sviluppo e Git | Issue, milestone, commit, branch breve, revisione, licenze e dati | Release 0.1 |
| Febbraio–marzo | 8 | Architettura a tre livelli | Presentazione, logica, persistenza, interfacce e test | Prototipo a livelli |
| Marzo–aprile | 14 | Concorrenza in Python | Thread, processi, stato condiviso, race condition, lock, semafori, code e deadlock | Laboratori, confronti sperimentali e test |
| Maggio | 8 | Project work | Coda concorrente, misure, documentazione, demo e retrospettiva | Release 1.0 e relazione |

## Progressione su processi e concorrenza

La Lezione **4.00 — Dal programma al processo: i primi thread in Python**
apre il percorso con un'esperienza concreta. I concetti vengono poi ripresi e
approfonditi nella sequenza seguente:

| Codice | Nucleo | Esperienza di laboratorio |
| --- | --- | --- |
| 4.00 | Dal programma al processo: i primi thread in Python | Confrontare due funzioni sequenziali con due oggetti `threading.Thread`; usare `start()` e `join()` |
| 4.01 | Thread e concorrenza | Avviare più thread, ripetere le esecuzioni, osservare l'ordine non deterministico e il comportamento del main thread |
| 4.02 | Stato condiviso | Far accedere più thread agli stessi dati e introdurre sperimentalmente il problema della race condition |
| 4.03 | Sincronizzazione con `Lock` | Individuare una sezione critica e confrontare `acquire()` / `release()` con il context manager `with lock:` |
| 4.04 | Coordinamento tra thread | Risolvere semplici problemi di coordinamento con `Semaphore` ed eventualmente `Event` |
| 4.05 | Produttore e consumatore | Modellare il problema e usare `queue.Queue` come struttura predisposta per lo scambio sicuro |
| 4.06 | Thread e processi | Confrontare memoria condivisa e memoria separata e introdurre il modulo `multiprocessing` |
| 4.07 | Concorrenza e parallelismo | Distinguere i due concetti, confrontare attività I/O-bound e CPU-bound e introdurre il GIL di CPython senza dettagli implementativi non necessari |
| 4.08 | Processi in Python | Usare `multiprocessing.Process`, `start()` e `join()` e confrontare sperimentalmente il comportamento con `threading` |
| 4.09 e successive | Consolidamento e mini-progetto | Risolvere piccoli problemi concorrenti, diagnosticare errori e integrare una coda concorrente nel progetto guida |

Il filo concettuale rimane:

```text
programma → processo → thread → concorrenza → stato condiviso
          → race condition → sincronizzazione → processi → parallelismo
```

## Metodo di lavoro

Ogni nucleo parte da un problema osservabile e procede per piccoli programmi
eseguibili. Prima dell'esecuzione gli studenti formulano una previsione; dopo
l'esecuzione raccolgono ciò che è accaduto, modificano il codice e confrontano
una versione problematica con una versione corretta.

Le definizioni formalizzano quanto osservato in laboratorio. I prodotti
richiesti sono script brevi, log o tabelle di confronto, spiegazioni del
comportamento e semplici test ripetibili, non trattazioni soltanto teoriche.

## Perché Python

Python permette di osservare rapidamente i concetti con le librerie standard
`threading`, `queue` e `multiprocessing`. Gli studenti possono concentrarsi
sull'ordine degli eventi, sullo stato condiviso e sui meccanismi di
sincronizzazione senza introdurre subito infrastrutture aggiuntive. Il
confronto tra thread e processi prepara inoltre la distinzione tra concorrenza
e parallelismo.

## Strumenti

| Strumento | Uso | Scelta operativa |
| --- | --- | --- |
| PlantUML | UML come testo | Strumento principale; diagrams.net solo per il primo schizzo |
| Git e GitHub | Storia, issue, release e revisione | Repository modello del docente; privati per gli studenti se disponibili |
| Python 3 | Processi, thread, sincronizzazione e code | Libreria standard; script brevi eseguibili dal terminale |
| VS Code | UML, Git e Python | Estensioni Python e PlantUML |
| `unittest` | Criteri e invarianti eseguibili | Pochi test significativi dopo le prime osservazioni |

Python è il linguaggio operativo del nucleo su processi e concorrenza. Le API
specifiche vengono introdotte soltanto quando servono a risolvere il problema
osservato.

## Valutazione

| Evidenza | Peso | Criteri |
| --- | ---: | --- |
| Requisiti e UML | 25% | Coerenza tra problema, requisiti e diagrammi |
| Git e architettura | 20% | Storia di lavoro e separazione dei livelli |
| Concorrenza | 30% | Correttezza, sincronizzazione e diagnosi |
| Project work | 25% | Integrazione, documentazione, demo e riflessione |

Per la concorrenza lo studente deve riconoscere una race condition, scegliere
il meccanismo più semplice adeguato, motivare terminazione e assenza di perdita
dei dati o stallo, e distinguere correttezza, prestazioni e leggibilità.

## Organizzazione dei materiali

Le lezioni usano codici `4.00`, `4.01`, `4.02` e successivi; i laboratori
possono usare, per esempio, `4.09-LAB-coda-concorrente`. Le prove valutative `CHK` restano su
Moodle.

Flusso: il sito spiega e avvia; il repository contiene codice e diagrammi;
Moodle riceve l'evidenza, restituisce feedback e gestisce il recupero.

## Prime quattro settimane

1. Lezione 4.00: dal programma al processo e primi thread in Python.
2. Apertura del repository modello, ambiente Python, convenzioni ed esecuzioni
   ripetibili.
3. Caso ticket: stakeholder, bisogno, confini e primi requisiti.
4. Requisiti funzionali/non funzionali, criteri di accettazione e commit della
   specifica v1.

## Continuità con TPSIT quinta

La distinzione tra processi, memoria condivisa e memoria separata prepara lo
studio successivo della comunicazione tra processi e dei socket. In quinta
questi prerequisiti verranno applicati ai servizi di rete senza duplicare i
laboratori di sincronizzazione svolti in quarta.

## Decisioni da verificare

Prima della scansione settimanale definitiva occorre verificare la versione di
Python disponibile nei laboratori, il comando di avvio e la presenza delle
estensioni necessarie in VS Code. La struttura resta valida; può cambiare il
tempo richiesto per uniformare l'ambiente.
