# AGENTS.md

## 1. Scopo e autorità del documento

Questo file è il contratto operativo permanente per Codex e per ogni altro
agente che interviene nel repository del sito didattico dell'Istituto
Archimede per l'anno scolastico 2026/27.

Il percorso di lavoro autorizzato è esclusivamente:

`C:\Github\didattica-archimede-2026-27`

Il repository `C:\Github\idoneita-terzo-anno`, quando disponibile, è una fonte
esterna in sola lettura: non deve mai essere modificato e i suoi vincoli
specifici non devono essere trasferiti automaticamente in questo progetto.

Le fonti hanno ruoli distinti:

- il prompt dell'utente definisce l'attività corrente, i file autorizzati e
  l'eventuale autorizzazione Git puntuale;
- `AGENTS.md` stabilisce le regole permanenti del repository;
- la roadmap del singolo percorso definisce progressione, contenuti, monte ore,
  ritmo e strumenti di quel corso;
- `PROGETTO.md` descrive finalità, architettura editoriale e principi generali;
- `README.md` descrive struttura e consultazione del repository;
- `_template-lezione/`, `_template-esercitazione/` e
  `docs/componenti.html` definiscono la struttura visuale e i componenti
  disponibili;
- i documenti originali in `fonti/` sono l'autorità sui materiali sorgente e
  restano locali e non pubblicabili.

Queste fonti non sono intercambiabili. Una roadmap non autorizza modifiche
estranee al prompt; un template non prevale sulla funzione didattica della
pagina; una regola generale non deve cancellare un vincolo specifico del corso.
Se due indicazioni risultano incompatibili, non scegliere silenziosamente:
conservare il lavoro esistente, descrivere il conflitto e chiedere istruzioni.

## 2. Checklist iniziale obbligatoria

Prima di creare o modificare una lezione, un'esercitazione o un materiale
didattico, completare nell'ordine i controlli pertinenti:

1. verificare che la directory corrente sia quella autorizzata;
2. verificare il branch corrente e leggere `git status --short --branch`;
3. leggere integralmente questo `AGENTS.md`;
4. individuare con precisione il percorso didattico interessato;
5. leggere la roadmap Markdown corrispondente e, in caso di dubbio sui
   contenuti, consultare la fonte originale in `fonti/` senza versionarla;
6. leggere l'indice HTML del percorso;
7. leggere la lezione precedente e, se esiste, quella successiva;
8. consultare il template pertinente e `docs/componenti.html`;
9. controllare eventuali modifiche preesistenti, incluse quelle non tracciate;
10. delimitare i soli file necessari all'attività e dichiarare qualsiasi
    sovrapposizione con lavoro già in corso;
11. verificare se collegamenti, indice o navigazione richiedano un adeguamento
    strettamente conseguente alla modifica richiesta;
12. distinguere prima di scrivere se il risultato è una presentazione, una
    lezione, un'esercitazione, un materiale integrativo, una verifica o una
    nota docente.

Se directory o branch sono errati, manca un documento autorevole oppure una
modifica preesistente non può essere isolata con sicurezza, fermarsi prima di
scrivere file.

## 3. Struttura del repository

La struttura principale è:

```text
assets/                  personalizzazioni CSS e JavaScript del progetto
docs/                    catalogo dei componenti
percorsi/                indici e contenuti dei cinque corsi
roadmap/                 roadmap autorevoli in Markdown
_template-lezione/       modello per le lezioni
_template-esercitazione/ modello per le esercitazioni
fonti/                   fonti, note docente e archivi locali ignorati da Git
index.html               portale generale dei percorsi
404.html                 pagina per risorse non trovate
```

Ogni lezione e ogni esercitazione deve stare in una cartella dedicata con
pagina principale `index.html`. Lezioni, esercitazioni, materiali integrativi
e note docente devono rimanere riconoscibili e separati. Non rinominare
cartelle o cambiare l'architettura del repository senza richiesta esplicita.

## 4. I cinque percorsi

Le informazioni seguenti derivano dalle roadmap reali. Prima di lavorare,
leggere comunque la roadmap completa del corso: la tabella è un orientamento,
non la sostituisce.

| Percorso | Cartella | Roadmap autorevole | Ore e durata orientativa | Strumenti principali | Vincoli specifici |
| --- | --- | --- | --- | --- | --- |
| Tecnologie informatiche — classi prime | `percorsi/tecnologie-informatiche-prime/` | `roadmap/tecnologie-informatiche-prime.md` | 2 ore settimanali; un incontro di circa 120 minuti, comprensivo di avvio e chiusura tecnica | Sito, Moodle, Google Drive, Documenti/Fogli/Presentazioni Google, simulatore Von Neumann, Flowgorithm portable; RapidTyping facoltativo | Laboratorio con carrellini; salvare su Drive, gestire account e riconsegna. Flowgorithm appartiene a questo percorso e non migra automaticamente negli altri. |
| TPSIT — classe terza | `percorsi/tpsit-terza/` | `roadmap/tpsit-terza.md` | 1 ora settimanale; lezioni tipiche da 55 minuti | Linux preconfigurato tramite WSL 2 o VM, VS Code, Python 3, Moodle | Ambiente minimo e uniforme; attività avviabili rapidamente; nessun progetto software lungo. Il filo conduttore è l'osservazione del sistema operativo. |
| TPSIT — classe quarta | `percorsi/tpsit-quarta/` | `roadmap/tpsit-quarta.md` | 2 ore settimanali; durata della singola lezione da adattare al blocco reale, non fissata ulteriormente dalla roadmap | PlantUML, Git e GitHub, Java 21 LTS, VS Code, JUnit; Maven dopo le basi, diagrams.net per il primo schizzo | Progettazione, UML, architettura e concorrenza. Verificare prima linguaggio di Informatica e disponibilità amministrativa di Java, WSL, VM ed estensioni. |
| Informatica — classi quinte | `percorsi/informatica-quinta/` | `roadmap/informatica-quinta.md` | 4 ore settimanali; ritmo consigliato di due incontri da 2 ore | Moodle, Git/GitHub, MariaDB, DBeaver, PHP 8.x, PDO, HTML/CSS, JavaScript essenziale, diagrams.net | Due gruppi con competenze comuni ma domini e dataset diversi. Sicurezza, query preparate, ruoli e difesa individuale sono parte del percorso. |
| TPSIT — classe quinta | `percorsi/tpsit-quinta/` | `roadmap/tpsit-quinta.md` | 3 ore settimanali in scansione 2+1: blocco da 2 ore e ora singola collegati | VS Code, Python 3, socket, Wireshark, Flask, HTML/CSS/JavaScript, JSON, Bruno, PWA, diagrams.net, Git/GitHub e Moodle | Il blocco lungo serve a costruire e collaudare; l'ora singola a progettare e verificare. Il coordinamento con Informatica non unifica repository, prove o criteri. |

Contenuti, linguaggi e strumenti non devono migrare automaticamente da un
corso all'altro. Prima di introdurre una tecnologia, verificarne la presenza
nella roadmap interessata o ottenere un'autorizzazione esplicita. In
particolare, non imporre Flowgorithm, Java, PHP, Flask, WSL, MariaDB o altri
strumenti al di fuori del percorso che li prevede.

## 5. Destinatari e livelli di contenuto

Ogni livello editoriale ha una funzione precisa:

- la **homepage generale** è il portale dei cinque percorsi e non una sequenza
  didattica unica;
- l'**indice del singolo corso** è il punto di accesso ordinario degli studenti
  di quella classe e disciplina;
- una **lezione pubblica** spiega e fa lavorare lo studente con contenuti
  consultabili e riutilizzabili;
- un'**esercitazione pubblica** contiene consegna, prerequisiti, file iniziali,
  criteri di completamento e aiuti progressivi, ma non soluzioni riservate;
- le **note docente** contengono regia, tempi, risposte attese, osservazioni,
  alternative e materiali non destinati agli studenti;
- **Moodle** gestisce consegne, verifiche, quiz, feedback, rubriche compilate,
  valutazioni, versioni facilitate, soluzioni e materiali riservati;
- `fonti/` conserva documenti originali, archivi e note locali non
  pubblicabili;
- Google Drive è un ambiente operativo previsto soprattutto per le classi
  prime, secondo la relativa roadmap;
- i repository di progetto contengono codice e documentazione versionata solo
  quando il percorso lo richiede.

Una pagina per studenti non deve diventare una programmazione annuale
completa, una scaletta minuto per minuto del docente, una rubrica interna o un
contenitore di istruzioni organizzative prive di utilità per lo studente. Le
scansioni temporali dettagliate e la regia vanno conservate, quando servono,
in note sotto `fonti/note-docente/<percorso>/<lezione>/`, che rimane ignorata
da Git.

## 6. Regole didattiche

### 6.1 Creazione e continuità delle lezioni

Ogni nuova lezione deve:

- rispettare roadmap, prerequisiti, livello della classe e progressione;
- collegarsi in modo naturale a quanto è già stato svolto;
- non anticipare argomenti successivi senza una richiesta esplicita e una
  motivazione didattica;
- partire, quando opportuno, da un problema, una domanda, un oggetto o una
  situazione concreta prima della formalizzazione;
- procedere con motivazione, spiegazione, esempio, attività e riepilogo;
- usare un linguaggio chiaro, diretto e tecnicamente corretto;
- graduare la difficoltà e distinguere concetti essenziali da
  approfondimenti;
- includere esempi e controesempi quando aiutano a delimitare un concetto;
- evitare sovraccarico cognitivo, ripetizioni e inventari troppo lunghi;
- proporre attività realistiche per il tempo e l'ambiente disponibili;
- essere coerente con dotazioni, account, rete e vincoli reali del
  laboratorio;
- produrre, quando pertinente, un'evidenza osservabile e riproducibile;
- non presentare come disponibile un file, un servizio o una lezione non
  ancora creati e verificati.

Il richiamo alla lezione precedente deve recuperare i prerequisiti senza
trasformarsi in una seconda lezione. La conclusione deve consolidare ciò che è
stato fatto e, se utile, preparare il passo successivo senza anticiparlo in
modo improprio.

Non imporre rigidamente tutte le sezioni a ogni pagina. Una presentazione di
corso, una lezione ordinaria, un laboratorio, un'esercitazione e una verifica
hanno funzioni diverse. La struttura deve restare riconoscibile e completa,
ma non produrre pagine artificialmente lunghe.

### 6.2 Introduzione del lessico tecnico

Ogni termine tecnico nuovo deve essere spiegato alla prima occorrenza. Ogni
acronimo deve essere prima scritto per esteso e poi accompagnato dalla sigla.
La definizione deve usare un linguaggio più semplice del termine definito e
non deve essere circolare né costruita con concetti ancora più difficili.

Quando è utile per la comprensione, la spiegazione deve comprendere:

- una definizione breve;
- un esempio concreto;
- un'analogia quotidiana, dichiarata chiaramente come semplificazione;
- una domanda di controllo.

Una lezione dovrebbe introdurre indicativamente non più di tre o quattro
termini nuovi importanti. Eventuali eccezioni devono essere motivate dal
contenuto. Quando compaiono almeno due termini nuovi, la pagina deve prevedere
un riquadro riconoscibile denominato **“Parole nuove”** o equivalente.

Distinguere chiaramente ciò che lo studente deve comprendere subito da ciò che
sarà approfondito nelle lezioni successive. Analogie ed esempi non devono
introdurre rappresentazioni tecnicamente errate. Uno stesso concetto deve
mantenere denominazione e significato coerenti nelle diverse lezioni e non si
devono presupporre conoscenze previste soltanto nelle parti successive della
roadmap. Per le classi fragili, suddividere le istruzioni operative in passi
brevi, osservabili e verificabili.

Prima di considerare completa una lezione, individuare tutti i termini tecnici
presenti e verificare che quelli non introdotti precedentemente siano definiti
o rimandati esplicitamente a una spiegazione successiva.

### 6.3 Materiali integrativi

Quaderni di allenamento, formulari, mappe, raccolte di esercizi e attività di
ripasso sono materiali integrativi, non nuove lezioni. Devono:

- dichiarare il percorso e la lezione o l'argomento di riferimento;
- consolidare argomenti già affrontati, salvo richiesta esplicita diversa;
- non alterare la numerazione delle lezioni;
- proporre attività graduate e teoria strettamente necessaria;
- rispettare le stesse regole di lingua, accessibilità e stile;
- collocare eventuali soluzioni secondo il corretto livello di riservatezza.

Prima di crearli, leggere la lezione di riferimento e verificare che il nuovo
materiale non duplicherà inutilmente contenuti già disponibili.

### 6.4 Coerenza editoriale

Dopo una modifica didattica controllare indice del percorso, lezione
precedente, lezione successiva, roadmap e collegamenti direttamente coinvolti.
Aggiornarli solo se necessario. Se sono già coerenti, non riscriverli e non
usare la richiesta come occasione per correzioni estranee.

## 7. Struttura consigliata delle lezioni

La struttura ordinaria comprende, quando pertinente:

1. codice, titolo e sottotitolo;
2. contesto o domanda iniziale;
3. durata, strumenti e prerequisiti;
4. raccordo con la lezione precedente;
5. obiettivi osservabili;
6. spiegazione progressiva;
7. esempio o dimostrazione;
8. attività guidata;
9. attività autonoma o variante, quando prevista;
10. errori frequenti e strategie di correzione;
11. riepilogo;
12. autoverifica o breve controllo finale;
13. glossario soltanto quando aggiunge reale utilità;
14. navigazione verso indice e lezioni adiacenti esistenti;
15. footer coerente con il progetto.

Una lezione di presentazione può privilegiare orientamento, domande e schemi;
un'esercitazione deve privilegiare consegna, procedura, aiuti e criteri di
completamento. Esercizi valutativi, soluzioni, rubriche compilate e feedback
devono essere collocati nell'ambiente riservato appropriato.

## 8. Accessibilità e inclusione

Ogni pagina pubblica deve essere progettata per l'uso reale da parte di una
classe eterogenea, anche in presenza di bisogni di lettura e organizzazione,
senza citare diagnosi o studenti specifici.

Verificare sempre:

- HTML5 semantico e landmark riconoscibili;
- un solo `h1` e gerarchia dei titoli senza salti ingiustificati;
- skip link funzionante verso il contenuto principale;
- navigazione completa da tastiera e focus chiaramente visibile;
- contrasto sufficiente in tema chiaro e scuro;
- rispetto di `prefers-reduced-motion`;
- layout leggibile su desktop, proiettore, tablet e smartphone;
- versione di stampa comprensibile e priva di elementi interattivi inutili;
- struttura prevedibile, paragrafi brevi e istruzioni sequenziali;
- informazioni non affidate esclusivamente a colore, posizione o movimento;
- tabelle usate solo per dati tabellari, con `caption`, intestazioni e `scope`
  quando necessari;
- campi di form associati a etichette esplicite e messaggi d'errore
  comprensibili;
- immagini informative con testo alternativo adeguato;
- immagini decorative con alternativa vuota quando appropriato;
- diagrammi leggibili, responsive e accompagnati da una rappresentazione
  semantica sufficiente;
- assenza di lampeggiamenti, animazioni superflue o interazioni che richiedano
  precisione motoria non necessaria.

Le immagini non devono essere l'unico mezzo per comunicare istruzioni o
concetti indispensabili. Se il testo alternativo diventerebbe troppo lungo,
aggiungere una spiegazione nel testo circostante.

## 9. Regole HTML

Ogni pagina HTML deve:

- iniziare con `<!doctype html>` e usare `<html lang="it">`;
- dichiarare `charset`, viewport, `title` descrittivo e meta description;
- usare correttamente `header`, `nav`, `main`, `section`, `article`, `aside` e
  `footer` secondo il significato, non come semplici contenitori grafici;
- avere un solo `main` e ID univoci;
- usare `aria-labelledby` e altri attributi ARIA solo quando validi e
  necessari;
- usare collegamenti relativi per pagine e risorse interne;
- rispettare esattamente maiuscole e minuscole dei nomi dei file;
- usare `index.html` come pagina principale di ogni cartella didattica;
- collegare soltanto destinazioni esistenti e verificate;
- evitare percorsi locali Windows, URL `file://` e percorsi assoluti del
  filesystem;
- evitare contenuti duplicati senza una ragione didattica;
- evitare markup superfluo prodotto da editor visuali;
- evitare CSS e JavaScript inline;
- mantenere breadcrumb, navigazione e footer coerenti con il livello della
  pagina.

Prima di aggiungere un attributo ARIA, preferire l'elemento HTML nativo che
esprime già il significato. Non usare `article` per blocchi che non sono
autonomi e non usare tabelle per ottenere un layout.

## 10. CSS, componenti e asset

Gli asset condivisi autorevoli sono pubblicati dal repository esterno
`mcocciniglia/common`. Le pagine devono continuare a caricare:

- `https://mcocciniglia.github.io/common/assets/style.css`;
- `https://mcocciniglia.github.io/common/assets/theme.css`;
- `https://mcocciniglia.github.io/common/assets/theme.js`;
- `https://mcocciniglia.github.io/common/assets/favicon.svg`.

Non creare una copia locale di `common/` e non sostituire gli asset autorevoli
con versioni semplificate. `assets/archimede.css` contiene soltanto le
personalizzazioni condivise del progetto; `assets/archimede.js` contiene
soltanto comportamento specifico realmente necessario.

Regole operative:

- non modificare il sistema visuale, la palette o la tipografia senza
  richiesta esplicita;
- non usare CSS inline;
- non introdurre framework CSS o dipendenze remote non autorizzate;
- prima di aggiungere una classe, verificare template e catalogo dei
  componenti;
- aggiungere componenti nuovi soltanto se riutilizzabili e privi di conflitti;
- mantenere nomi di classi descrittivi e non legati a una singola frase;
- rendere le immagini responsive con proporzioni stabili e senza scorrimento
  orizzontale;
- preferire SVG per schemi e diagrammi precisi, mantenendo testo alternativo e
  semantica adeguati;
- usare nomi file descrittivi, minuscoli e coerenti, salvo vincoli esistenti;
- non spostare o rinominare asset senza aggiornare e verificare ogni
  riferimento;
- verificare sempre tema chiaro, tema scuro, responsive e stampa.

## 11. JavaScript e codice eseguibile

JavaScript deve essere usato soltanto quando aggiunge una funzione reale che
HTML e CSS non possono offrire in modo adeguato. Non deve nascondere o
sostituire contenuti essenziali disponibili in HTML.

- non introdurre framework, librerie o servizi senza autorizzazione;
- mantenere un comportamento comprensibile senza JavaScript, quando possibile;
- usare `assets/archimede.js` solo per funzioni comuni specifiche del progetto;
- lasciare la gestione del tema all'asset comune `theme.js` e mantenere la
  compatibilità con `#themeToggle` e `.btn-label`;
- ridurre manipolazioni DOM, eventi e stato al minimo necessario;
- evitare dipendenze da account o rete non dichiarate.

Esempi di codice, programmi, comandi, starter e configurazioni devono essere
eseguiti o verificati nell'ambiente previsto dalla roadmap prima della
pubblicazione. Non inserire mai credenziali, token, password, chiavi o segreti.
Le configurazioni sensibili devono usare variabili d'ambiente e file ignorati,
con esempi pubblici privi di valori reali.

## 12. Navigazione e stato dei contenuti

L'indice del percorso rappresenta la sequenza realmente disponibile. Una
lezione può essere collegata come disponibile solo quando il relativo file
esiste, è stato verificato e appartiene al percorso corretto.

- non creare link vuoti, `href="#"` usati come segnaposto o collegamenti a
  pagine inesistenti;
- non usare la pagina `404.html` come sostituto di una destinazione futura;
- i contenuti futuri possono essere descritti come “previsti” o “in
  preparazione”, ma non devono apparire pubblicati;
- breadcrumb e navigazione precedente/successiva devono corrispondere alla
  posizione reale;
- non mostrare un link alla lezione successiva finché la destinazione non
  esiste, salvo diverso comportamento già progettato e autorizzato;
- quando si crea o si rinomina una pagina, controllare tutti i riferimenti
  interni coinvolti;
- la homepage generale deve mantenere separati i cinque percorsi;
- ogni studente deve poter raggiungere direttamente l'indice del proprio
  corso senza attraversare contenuti di altre classi.

Non aggiungere automaticamente pagine placeholder. Un file mancante, un nome
errato o un asset non trovato devono restare errori da correggere, non essere
mascherati come contenuti in preparazione.

## 13. Identità del docente

Tutte le pagine HTML pubbliche devono mostrare nel footer la dicitura:

> **Docente: Prof. Marco Cocciniglia**

La dicitura deve essere mantenuta durante revisioni, semplificazioni e
rigenerazioni. Il footer deve conservare anche materia, classe e anno
scolastico quando pertinenti. Il nome del docente non deve essere duplicato
nello stesso footer né spostato nell'hero senza richiesta esplicita.

## 14. Privacy e separazione tra pubblico e riservato

Non pubblicare nel sito o nel repository:

- nomi o dati identificativi degli studenti;
- voti, valutazioni, feedback personali o rubriche compilate;
- elaborati o fotografie riconducibili a studenti;
- indirizzi email personali;
- credenziali, password, token, chiavi o segreti;
- soluzioni riservate o materiali di verifica non destinati al pubblico;
- materiali protetti, licenze incompatibili o contenuti non autorizzati.

La separazione degli ambienti è obbligatoria:

- GitHub Pages ospita esclusivamente contenuti pubblici;
- Moodle ospita consegne, verifiche, feedback, valutazioni e riservati;
- `fonti/` ospita sorgenti originali, archivi e note locali;
- eventuali repository privati ospitano codice degli studenti solo quando la
  roadmap e l'organizzazione scolastica lo prevedono.

`fonti/` deve rimanere esclusa da Git. Nessun DOCX o archivio ZIP deve essere
versionato. Non copiare nel progetto cartelle `.git`, metadati di repository o
file nascosti provenienti dagli archivi. Prima di pubblicare, cercare anche
chiavi private, file `.env`, certificati e nomi file che suggeriscano segreti.

## 15. Limiti delle modifiche

Codex e gli altri agenti devono:

- modificare esclusivamente i file richiesti o quelli strettamente necessari
  alla coerenza dell'attività autorizzata;
- preservare ogni modifica preesistente dell'utente o di altri lavori;
- non riformattare, riordinare o normalizzare file estranei;
- non cambiare struttura, navigazione generale, stile o strumenti senza
  autorizzazione;
- non eliminare contenuti prima di comprenderne funzione, autorevolezza e
  destinazione;
- non rinominare cartelle o file se non richiesto;
- non correggere automaticamente problemi estranei: segnalarli separatamente;
- fermarsi quando una richiesta si sovrappone a lavoro esistente e non può
  essere isolata con sicurezza.

Piccoli aggiornamenti a indice o navigazione sono ammessi solo se indispensabili
per rendere raggiungibile e coerente il contenuto richiesto. Devono essere
spiegati nel resoconto finale.

## 16. Controlli obbligatori

Prima di considerare conclusa una modifica, eseguire per quanto pertinente:

1. controllo della struttura e validità HTML;
2. `git diff --check`;
3. verifica di tutti i link, frammenti e riferimenti locali coinvolti;
4. verifica di esistenza e corretta capitalizzazione dei file;
5. controllo di title, description, unico `h1`, titoli, ID e landmark;
6. controllo di accessibilità semantica e uso da tastiera;
7. verifica di focus visibile e contrasto;
8. tema chiaro e tema scuro;
9. responsive su viewport coerenti con desktop, tablet e smartphone;
10. stampa;
11. `prefers-reduced-motion`;
12. grammatica, ortografia e chiarezza delle istruzioni;
13. correttezza tecnica ed eseguibilità degli esempi;
14. coerenza con roadmap, indice e lezioni adiacenti;
15. ricerca di credenziali, chiavi, dati personali e materiali riservati;
16. verifica che `fonti/`, DOCX e ZIP restino ignorati e non tracciati;
17. controllo dello stato Git e dell'elenco esatto dei file modificati;
18. riepilogo finale di modifiche, controlli superati e limiti della verifica.

Non dichiarare un controllo non eseguito. Se il browser visuale non è
disponibile, dichiararlo esplicitamente: i controlli statici su CSS e markup
non equivalgono a una verifica visuale completa. Se un validatore o un servizio
esterno non è raggiungibile, indicare il controllo alternativo svolto.

## 17. Politica Git

### 17.1 Sempre consentito

Sono consentite le operazioni non modificanti necessarie a capire e verificare
il repository:

- `git status`;
- `git diff`;
- consultazione della cronologia;
- verifica di branch e remoti;
- test e controlli sui file che non cambiano contenuti o configurazione.

`git fetch` aggiorna riferimenti locali e va eseguito solo quando richiesto o
necessario e autorizzato dall'attività corrente.

### 17.2 Regola ordinaria

Il lavoro ordinario avviene su `develop`. Codex può modificare i file richiesti,
ma non deve automaticamente:

- eseguire `git add`;
- creare commit;
- eseguire push;
- creare o eliminare branch;
- effettuare merge, rebase o cherry-pick;
- creare tag o pull request;
- modificare remoti o configurazione Git;
- modificare la configurazione di GitHub Pages.

### 17.3 Autorizzazioni puntuali

- commit e push su `develop` sono consentiti soltanto se richiesti
  esplicitamente nell'attività corrente;
- l'autorizzazione vale esclusivamente per i file e lo scopo indicati e non si
  trasferisce alle attività successive;
- merge o push verso `main` richiedono una seconda autorizzazione esplicita e
  separata, impartita dopo la verifica del materiale su `develop`;
- prima di operare su `main`, controlli, revisione e pubblicazione su
  `develop` devono risultare completati, salvo diversa istruzione esplicita;
- un'autorizzazione al commit non autorizza il push, e un'autorizzazione al
  push su `develop` non autorizza `main`, se il prompt non lo dichiara.

Prima di ogni commit autorizzato:

1. verificare il branch corrente;
2. mostrare o riepilogare lo stato Git;
3. controllare il diff e l'elenco dei file da includere;
4. escludere modifiche preesistenti o estranee;
5. completare i controlli previsti dal progetto;
6. verificare l'assenza di credenziali, dati personali e materiali riservati;
7. verificare che `fonti/`, DOCX e ZIP non siano inclusi;
8. usare staging esplicito dei soli file autorizzati, mai inclusione
   automatica indiscriminata.

### 17.4 Sempre vietato senza richiesta eccezionale e inequivocabile

- force push;
- riscrittura della cronologia;
- `git reset --hard`;
- eliminazione o sovrascrittura di modifiche dell'utente;
- inclusione automatica di file estranei;
- comandi distruttivi non indispensabili e non esplicitamente autorizzati;
- pubblicazione di `fonti/`, DOCX, ZIP, segreti o materiali riservati;
- copie di cartelle `.git` provenienti da archivi o repository sorgente.

Se il working tree contiene modifiche non riconducibili all'attività, lasciarle
intatte. Se non è possibile isolare con certezza i file autorizzati, fermarsi
e chiedere indicazioni invece di eseguire staging, commit o pulizia.

## 18. Regola finale

Prima di intervenire, comprendere corso, destinatario, posizione nella roadmap
e stato del repository. Modificare soltanto ciò che è richiesto, verificare
integralmente il risultato e non pubblicare senza autorizzazione esplicita.
