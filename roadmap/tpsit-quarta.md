# TPSIT — classe quarta

Anno scolastico 2026/27 · 2 ore settimanali · circa 60 ore nominali

## Visione del percorso

Il filo conduttore dell'anno è:

```text
Web dinamico → JavaScript → API → cloud → IoT → IA
```

Gli studenti passeranno da una pagina Web statica a semplici applicazioni
capaci di reagire alle azioni dell'utente, scambiare dati con servizi remoti e
comunicare con dispositivi reali. Il cloud computing, l'Internet delle cose
(Internet of Things, IoT) e l'intelligenza artificiale (IA) saranno introdotti
attraverso attività osservabili, non come raccolte di definizioni astratte.
Ingegneria del software e UML essenziale accompagneranno i laboratori con un
ruolo applicativo.

## Obiettivo annuale

Realizzare e spiegare una piccola applicazione interattiva e connessa, sapendo
riconoscere il ruolo dell'interfaccia Web, dei dati e di un servizio o di
un'interfaccia di programmazione delle applicazioni (Application Programming
Interface, API) e, quando previsto dall'attività, di un dispositivo Shelly o di
un semplice modello di IA.

Il risultato finale non deve necessariamente usare tutte le tecnologie
incontrate. Deve invece mostrare una catena di funzionamento comprensibile,
verificata per passi e documentata con gli strumenti più semplici adeguati.

## Impostazione didattica

Il percorso è laboratoriale, graduale e concreto. Ogni nuovo concetto parte da
un comportamento visibile e conduce a una piccola evidenza verificabile.

Per sostenere una classe fragile:

- si affronta un obiettivo operativo alla volta;
- le consegne sono divise in passi brevi con checkpoint frequenti;
- un esempio guidato precede la variante autonoma;
- prima di eseguire si formula una previsione, poi si osserva e si corregge;
- il codice iniziale resta breve e viene esteso solo dopo una verifica;
- ogni attività prevede un risultato minimo raggiungibile e un'estensione
  facoltativa;
- quando rete, account o dispositivi non sono disponibili si usa una prova
  locale o una dimostrazione preparata dal docente;
- le evidenze individuali restano riconoscibili anche nelle attività svolte in
  coppia o in piccolo gruppo.

## Monte ore

- 54 ore pianificate;
- 6 ore di margine per recupero, problemi tecnici, consolidamento e
  riallineamento.

## Roadmap annuale

### Nuclei didattici

| Periodo indicativo | Ore | Nucleo | Attività prevalente | Evidenza osservabile |
| --- | ---: | --- | --- | --- |
| Settembre–novembre | 14 | 1. JavaScript e Web dinamico | Dalla console del browser a una pagina che reagisce a input ed eventi | Pagina Web interattiva |
| Novembre–dicembre | 6 | 2. API e comunicazione con servizi | Inviare una richiesta, leggere una risposta e usare dati JSON | Piccolo client di un servizio |
| Gennaio | 6 | 3. Cloud computing | Confrontare esecuzione locale e servizio remoto; pubblicare una semplice applicazione quando possibile | Applicazione o demo raggiungibile |
| Febbraio–marzo | 8 | 4. IoT con dispositivi Shelly | Leggere lo stato e inviare comandi nella rete locale | Controllo ripetibile di un dispositivo |
| Marzo–aprile | 8 | 5. Intelligenza artificiale | Addestrare e provare un semplice classificatore | Modello sperimentale e prove commentate |
| Distribuite durante l'anno | 4 | 6. Ingegneria del software | Definire, costruire, provare, distribuire e correggere il prodotto | Checklist e breve documentazione |
| Distribuite durante l'anno | 2 | 7. UML essenziale | Rappresentare interazioni realmente progettate | Uno o più diagrammi utili al progetto |

### Progetto guida trasversale · IoT e IA

Alle 48 ore dedicate ai sette nuclei si affiancano 6 ore di integrazione,
distribuite durante l'anno e concentrate nei checkpoint conclusivi. Il
progetto **Dal comando digitale all'azione reale** collega almeno due parti
del percorso in un prototipo comprensibile e in una breve dimostrazione.

Le ore di ingegneria del software e UML sono distribuite nei laboratori. Il
progetto guida non è un ottavo nucleo e non costituisce un blocco teorico
separato.

## Flessibilità della roadmap

La scansione non è rigida: profondità e durata dei nuclei saranno adattate al
ritmo reale della classe e alle evidenze raccolte durante i laboratori.

- JavaScript, API e IoT possono ricevere più tempo quando serve consolidare i
  prerequisiti o completare un'esperienza funzionante;
- cloud, IA e UML possono essere modulati senza perdere il filo essenziale del
  percorso;
- le 6 ore di margine assorbono recupero, problemi tecnici e riallineamento;
- Python resta uno strumento laboratoriale per API e IoT, non un corso di
  programmazione parallelo;
- non viene reintrodotto un percorso autonomo sul multithreading.

## 1. JavaScript e Web dinamico

### Domanda guida

Come può una pagina Web reagire alle azioni dell'utente?

### Contenuti essenziali

- console del browser;
- variabili e tipi;
- condizioni e cicli;
- funzioni;
- array;
- Document Object Model (DOM), cioè la rappresentazione della pagina che
  JavaScript può leggere e modificare;
- eventi;
- collegamento e interazione tra HTML e JavaScript.

### Laboratorio ed evidenza

Si parte da istruzioni eseguite nella console e si passa gradualmente a uno
script collegato a una pagina HTML. Pulsanti, campi di input e messaggi
permettono di osservare subito l'effetto del codice. L'evidenza minima è una
pagina che riceve un dato, esegue una semplice elaborazione e aggiorna il
contenuto mostrato.

## 2. API e comunicazione con servizi

### Domanda guida

Come può un'applicazione chiedere dati o un'operazione a un altro sistema?

### Contenuti essenziali

- richiesta e risposta;
- dati strutturati in formato JavaScript Object Notation (JSON);
- ruolo di una API;
- uso guidato di un servizio remoto;
- controllo dei dati ricevuti e gestione essenziale degli errori.

### Laboratorio ed evidenza

Gli studenti osservano una richiesta reale, leggono la risposta e individuano
i dati utili. In seguito li mostrano in una pagina o in un piccolo programma.
L'obiettivo è comprendere la catena seguente senza trasformare il nucleo in un
corso teorico sui protocolli:

```text
applicazione → API → servizio remoto
```

## 3. Cloud computing

### Domanda guida

Che cosa cambia quando un'applicazione o un servizio non si trova sul nostro
computer?

### Contenuti essenziali

- differenza tra risorsa locale e risorsa remota;
- servizi cloud e servizi per sviluppatori;
- hosting;
- deployment, inteso come pubblicazione controllata di un'applicazione;
- Software as a Service (SaaS), Platform as a Service (PaaS) e Infrastructure
  as a Service (IaaS) a livello introduttivo.

### Laboratorio ed evidenza

Si confrontano esempi concreti già noti agli studenti e, se account e rete lo
consentono, si pubblica una piccola applicazione. Non è richiesto configurare
infrastrutture complesse: è sufficiente saper distinguere ciò che viene
eseguito localmente da ciò che è fornito o pubblicato a distanza.

## 4. IoT con dispositivi Shelly

### Domanda guida

Come può un programma leggere o comandare un oggetto reale attraverso la rete?

### Contenuti essenziali

- dispositivo connesso;
- comunicazione nella rete locale;
- richieste alle API del dispositivo;
- lettura dello stato;
- invio di un comando;
- differenza tra sensore e attuatore.

### Laboratorio ed evidenza

I dispositivi Shelly sono un caso concreto che unisce rete, API,
programmazione e automazione. Python è usato esclusivamente come strumento
laboratoriale per preparare e inviare richieste brevi; non apre un secondo
percorso di programmazione parallelo.

```text
programma Python → richiesta → API → rete locale
                                      ↓
                         dispositivo Shelly
                                      ↓
                           sensore o attuatore
```

L'evidenza minima è una sequenza ripetibile che legge uno stato oppure invia
un comando a un dispositivo predisposto dal docente.

## 5. Intelligenza artificiale

### Domanda guida

Che differenza c'è tra una regola scritta nel codice e una previsione prodotta
da un modello?

### Contenuti essenziali

- riconoscimento di immagini;
- riconoscimento vocale;
- classificazione;
- dati di esempio e addestramento;
- semplice modello sperimentale con Teachable Machine;
- eventuale uso del modello in un'applicazione.

### Laboratorio ed evidenza

Gli studenti preparano poche classi distinguibili, addestrano un modello e lo
provano con esempi nuovi. Annotano almeno un risultato corretto e un errore,
senza presentare il modello come infallibile. Se tempo e strumenti lo
consentono, la previsione viene letta da una semplice applicazione.

La distinzione da mantenere è:

```text
automazione tradizionale: sensore → condizione esplicita → azione
sistema con IA:           dati → modello → previsione → azione
```

## Progetto guida trasversale · IoT e IA

### Dal comando digitale all'azione reale

Il progetto guida collega progressivamente API, cloud, IoT, IA e progettazione
software. Non è un prodotto separato da costruire tutto alla fine e non
richiede che ogni gruppo realizzi tutte le varianti possibili.

```text
utente → interfaccia → software → servizio o modello
        → API → Shelly → dispositivo reale
```

Possibili sviluppi sono un comando digitale che accende una luce, un gesto
riconosciuto tramite webcam, la lettura di un sensore, il controllo con un
breve programma Python o la visualizzazione dello stato in una pagina Web.
Sono opzioni da scegliere in base al tempo e alle dotazioni, non promesse di
realizzazione simultanea.

Il prodotto minimo deve collegare almeno due parti della catena, funzionare in
una dimostrazione breve e permettere allo studente di spiegare che cosa accade
in ogni passaggio.

## 6. Ingegneria del software

L'ingegneria del software accompagna le attività invece di diventare un
modulo soltanto teorico. Requisiti, progettazione, implementazione, test,
distribuzione e manutenzione vengono applicati ai prodotti costruiti durante
l'anno. Per ogni prodotto significativo gli studenti usano una versione
essenziale di questo ciclo:

1. chiarire il bisogno e scrivere pochi requisiti verificabili;
2. progettare i passaggi e l'interfaccia minima;
3. implementare una parte alla volta;
4. eseguire prove ripetibili;
5. distribuire o presentare il prodotto nell'ambiente previsto;
6. correggere e mantenere una versione funzionante.

L'evidenza può essere una checklist breve con requisito, prova svolta, esito e
correzione effettuata.

## 7. UML essenziale

Quando utile al progetto, useremo alcuni semplici diagrammi Unified Modeling
Language (UML) per descrivere sistemi realmente progettati o realizzati,
soprattutto casi d'uso, attività e sequenze.

Si privilegiano:

- diagramma dei casi d'uso per chiarire attori e obiettivi;
- diagramma delle attività per ordinare decisioni e azioni;
- diagramma di sequenza per rappresentare lo scambio tra applicazione, API,
  servizio e dispositivo;
- diagramma delle classi come approfondimento eventuale, soltanto quando le
  classi del prodotto rendono il diagramma realmente utile.

È sufficiente un diagramma leggibile, coerente con il prodotto e spiegabile
dallo studente. PlantUML o diagrams.net possono essere scelti in base alla
semplicità del caso e alla disponibilità degli strumenti.

## Metodo di lavoro

Ogni laboratorio segue una sequenza riconoscibile:

1. osservare un esempio o un problema concreto;
2. formulare una previsione;
3. costruire o modificare una parte piccola;
4. eseguire e raccogliere un risultato;
5. confrontare il risultato con il comportamento atteso;
6. correggere, salvare e spiegare ciò che è stato verificato.

Le definizioni arrivano dopo la prima osservazione e usano lo stesso lessico
della pagina indice e delle lezioni. Le estensioni non devono impedire il
raggiungimento dell'obiettivo minimo.

## Strumenti

| Strumento | Uso | Scelta operativa |
| --- | --- | --- |
| Browser e strumenti di sviluppo | Console, DOM, eventi, richieste e risposte | Un solo browser di riferimento in laboratorio |
| HTML, CSS e JavaScript | Interfaccia e comportamento delle applicazioni Web | File brevi e struttura iniziale fornita quando utile |
| JSON e API selezionate | Scambio di dati con servizi | Esempi stabili, senza credenziali pubblicate |
| Servizio di hosting o cloud | Pubblicazione e confronto locale/remoto | Solo se account, rete e condizioni d'uso sono disponibili |
| Dispositivi Shelly e rete locale | Esperienze IoT con sensori e attuatori | Dispositivi predisposti dal docente e prove controllate |
| Python 3 | Invio di richieste alle API dei dispositivi | Solo script brevi per il laboratorio IoT/API |
| Teachable Machine | Addestramento di un semplice modello | Dati non personali e attività guidata |
| PlantUML o diagrams.net | UML essenziale | Scegliere lo strumento più semplice per il diagramma richiesto |
| Git e GitHub | Conservazione delle versioni e documentazione | Supporto al progetto, non nucleo autonomo; usarli se disponibili |
| Moodle | Consegne, verifiche, feedback e recupero | Materiali riservati fuori dal sito pubblico |

## Valutazione

Le prove sono brevi, distribuite e collegate a prodotti osservabili. Il peso
indicativo delle evidenze è:

| Evidenza | Peso | Criteri principali |
| --- | ---: | --- |
| JavaScript e Web dinamico | 25% | Correttezza, interazione visibile e capacità di spiegare il codice |
| API e cloud | 20% | Lettura dei dati, distinzione locale/remoto e gestione degli errori essenziali |
| IoT | 20% | Sequenza di comunicazione corretta e prova ripetibile sul dispositivo |
| Intelligenza artificiale | 15% | Addestramento controllato, prove e distinzione dall'automazione tradizionale |
| Progetto, documentazione e UML | 20% | Integrazione, test, chiarezza della dimostrazione e coerenza dei diagrammi |

La valutazione non dipende dalla disponibilità domestica di account,
dispositivi o servizi. Le attività che richiedono dotazioni specifiche si
svolgono nell'ambiente predisposto dalla scuola.

## Organizzazione dei materiali

Le lezioni usano codici `4.00`, `4.01`, `4.02` e successivi. Eventuali
laboratori collegati mantengono un nome riconoscibile e dichiarano il prodotto
atteso. Il sito presenta e avvia le attività; gli eventuali repository
conservano codice e documentazione; Moodle riceve le evidenze, restituisce
feedback e gestisce prove e recupero.

Una lezione viene collegata dall'indice soltanto dopo essere stata creata e
verificata. La roadmap descrive anche contenuti futuri, ma non li presenta come
materiali già pubblicati.

## Prime quattro settimane

1. Lezione 4.00: dalla pagina statica al primo JavaScript, usando la console
   del browser e uno script collegato al documento HTML.
2. Variabili, tipi e semplici trasformazioni di dati con risultato visibile.
3. Condizioni ed eventi per reagire a un pulsante o a un input.
4. Funzioni, primi array e modifica guidata del DOM in una piccola pagina.

## Continuità con TPSIT quinta

La comprensione di richiesta, risposta, API, servizi remoti, rete locale e
cloud prepara lo studio dei servizi di rete e delle applicazioni distribuite
in quinta. La continuità riguarda i concetti e il metodo di osservazione; non
richiede di anticipare in quarta gli strumenti specifici del percorso
successivo.

## Decisioni da verificare

Prima della scansione settimanale definitiva occorre verificare:

- browser ed editor disponibili nel laboratorio;
- accesso ai servizi cloud e condizioni per la pubblicazione;
- disponibilità dei dispositivi Shelly e loro configurazione nella rete
  locale;
- comando Python utilizzabile sulle postazioni per le sole esperienze IoT;
- accesso a Teachable Machine e possibilità di usare webcam o microfono senza
  raccogliere o pubblicare dati personali;
- disponibilità di PlantUML, diagrams.net e degli eventuali account GitHub;
- attività locali alternative per gli incontri in cui rete o servizi remoti
  non siano disponibili.
