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
| Settembre | 2 | Allineamento | Repository, convenzioni, compilazione ed esecuzione | Repository funzionante |
| Settembre–ottobre | 6 | Requisiti | Stakeholder, requisiti, user story, criteri e tracciabilità | Specifica v1 e matrice |
| Ottobre–novembre | 10 | UML essenziale | Casi d'uso, attività, classi, sequenza e stati | Dossier UML versionato |
| Dicembre–gennaio | 6 | Ciclo di sviluppo e Git | Issue, milestone, commit, branch breve, revisione, licenze e dati | Release 0.1 |
| Febbraio–marzo | 8 | Architettura a tre livelli | Presentazione, logica, persistenza, interfacce e test | Prototipo a livelli |
| Marzo–aprile | 14 | Concorrenza in Java | Thread, task, race condition, lock, semafori, code e deadlock | Laboratori e test |
| Maggio | 8 | Project work | Coda concorrente, misure, documentazione, demo e retrospettiva | Release 1.0 e relazione |

## Perché Java

Java rende espliciti `Thread`, `Runnable`, `ExecutorService`, `synchronized`,
`Lock`, `Semaphore` e `BlockingQueue` senza dipendenze esterne. Mantiene anche
il collegamento tra diagramma delle classi, codice e test. Le virtual thread
sono un'estensione finale, non il punto di partenza.

## Strumenti

| Strumento | Uso | Scelta operativa |
| --- | --- | --- |
| PlantUML | UML come testo | Strumento principale; diagrams.net solo per il primo schizzo |
| Git e GitHub | Storia, issue, release e revisione | Repository modello del docente; privati per gli studenti se disponibili |
| Java 21 LTS | Concorrenza esplicita e testabile | API standard; Maven soltanto dopo le basi |
| VS Code | UML, Git e Java | Extension Pack for Java e PlantUML |
| JUnit | Criteri e invarianti eseguibili | Pochi test significativi |

Se Informatica usa già Java, TPSIT lo applica a progettazione e concorrenza.
Se usa un altro linguaggio, si prevedono 4 ore iniziali di Java sottratte al
project work, non alla sincronizzazione.

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

Le lezioni usano codici `4.01`, `4.02` e successivi; i laboratori usano, per
esempio, `4.08-LAB-race-condition`. Le prove valutative `CHK` restano su
Moodle.

Flusso: il sito spiega e avvia; il repository contiene codice e diagrammi;
Moodle riceve l'evidenza, restituisce feedback e gestisce il recupero.

## Prime quattro settimane

1. Apertura del repository modello, compilazione ed esecuzione.
2. Caso ticket: stakeholder, bisogno e confini.
3. Requisiti funzionali/non funzionali e criteri di accettazione.
4. Primo caso d'uso PlantUML e commit della specifica v1.

## Decisioni da verificare

Prima della scansione settimanale definitiva occorre confermare il linguaggio
usato in Informatica e i vincoli amministrativi relativi a WSL, VM, Java ed
estensioni. La struttura resta valida; può cambiare il tempo di avvio.

