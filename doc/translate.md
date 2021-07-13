# Istruzioni per traduttori


Risorse | Link
--------|:----:
Obbligatorie | [[Guidelines linguistiche]](https://drive.google.com/file/d/1GuYx3r637srhyxY2QYfKYO9Jbka-_gKd/view?usp=sharing)
Consigliate | [[Telegram Web]](https://web.telegram.org), [[Telegram Desktop]](https://desktop.telegram.org/)


## Setup

Per poter contribuire alla traduzione, dopo aver letto le [guidelines
 linguistiche](https://drive.google.com/file/d/1GuYx3r637srhyxY2QYfKYO9Jbka-_gKd/view?usp=sharing)
occorre:

1. creare (gratuitamente) un account su
   [GitHub](https://www.github.com) ("Sign Up" e seguire la procedura
   sino a verificare la mail);
   
2. comunicarmi lo username GitHub con cui intendete collaborare, per
   [abilitazione](../data/users.csv). 

	Verrà risposto un nome file di prova: tradurlo e sottomettere la
	revisione, *come illustrato nel seguito* (occorre leggere fino a
	fine pagina per saper cosa/come fare).
	
	Una volta fatto, se ci si sente ragionevolmente a proprio agio con
    la procedura di modifica/sottomissione si può passare allo step
    successivo, alternativamente si può chiedere
	
	```
	@lucailgarb #sandbox
	```
	per la predisposizione di un altro file di prova;

3. per richiedere l'assegnazione di uno spezzone di sottotitoli postare:
   
	```
	@lucailgarb #translate
	```


## Il file su cui lavoriamo per la traduzione

Il file su cui dobbiamo operare è stato generato da un software
speech-to-text a partire dal video originale.

Per quanto riguarda il riconoscimento delle parole (soprattutto in
inglese e quando l'audio è chiaro) oramai questi software fanno
abbastanza "paura"; quello che ancora fanno fatica a capire sono i
toni (es quindi fanno fatica a capire le domande, la punteggiatura
ecc). 

Ma qui entrate in gioco voi e l'*imprescindibilità*, quando si andrà a
tradurre e preparare i subs, di *ascoltare/guardare* il video.


### Formato sottotitoli 

Informaticamente i sottotitoli si trovano in un file `.srt` ossia un
file di testo (tipo `.txt`) con una struttura precisa, da
rispettare/non modificare.

Ad esempio, di seguito uno stralcio per i primi secondi del video che
usiamo ai cubi:

```
1
00:00:00,000 --> 00:00:01,200
Prodotti caseari

2
00:00:02,000 --> 00:00:24,000
Inseminazione forzata

3
00:00:33,000 --> 00:00:49,000
Separazione dei neonati

4
00:00:51,000 --> 00:01:04,000
Questa è una pratica standard
```

Per ogni sottotitolo vi è dunque:
* un numero progressivo;
* i secondi di inizio e fine della sua visualizzazione;
* il testo (che può essere organizzato su più righe);
* una linea bianca di separazione.

Questo file (tradotto in italiano) è quello a cui dobbiamo, *alla fine
di tutto*, arrivare.


### Come/cosa modificare

Per permettere la **revisione** delle traduzioni, i traduttori
lavorano su un file *lievemente diverso*, che includa sia l'originale
che la traduzione. Uno stralcio/esempio del file che otterrete:

```
3
00:00:33,000 --> 00:00:49,000
## Newborn separation



4
00:00:51,000 --> 00:01:04,000
## This is standard practice



```

Quello che dovrete fare è la cosa seguente:
* lasciare **tutto immutato**;
* **aggiungere la/e linea/e tradotta/e** in italiano sotto a quella inglese;
* **lasciare almeno una linea di spazio** alla fine.

Come segue:
```
3
00:00:33,000 --> 00:00:49,000
## Newborn separation
Separazione dei neonati



4
00:00:51,000 --> 00:01:04,000
## This is standard practice
Questa è pratica standard



```


## Il processo step-by-step

Per lavorare alle traduzioni:

0. nel gruppo Telegram "AV: Traduzioni e Sub YouTube" postare:

	```
	@lucailgarb #translate
	```
	Per richiedere l'assegnazione di un file da tradurre.
	Verrà risposto (quanto prima) un messaggio con la posizione del 
	file, del tipo:
	
	```
	subs/hnva2/subs_012000_lbraglia.srt
	```
	che sta a significare: ti è stato assegnato
	
	* il file `subs_012000_lbraglia.srt` (uno
	spezzone di sottotitoli che inizia approssimativamente a
	`01:20:00` nel video) 
	* che si trova nella cartella `hnva2` (che contiene i sottotitoli
	per "Holding Non-Vegans Accountable 2.0") 
	* posta nella cartella `subs` (che racchiude tutti i
	sottotitoli di tutti i video).

1. da **computer**, effettuare il login su [GitHub](https://www.github.com);

2. aprire [questa](https://github.com/av-italia/subs) pagina, dove sono
   conservate le traduzioni;

3. cliccare quindi sulla cartella `subs`
   
   ![subs dir](../img/subs_dir.png)

4. cliccare sulla cartella del video (`hnva2` nell'esempio)

	![hnva2 dir](../img/hnva2_dir.png)

5. arrivati a questo punto conviene **salvare questa pagina nei
   preferiti** (per accedervi facilmente alle prossime sessioni)
   perché tutte i file di un dato video si trovano qui e si
   velocizzerà l'accesso al file assegnato.

   Cliccare dunque sul nome del file che ci è stato assegnato
   (`subs_012000_lbraglia.srt` nell'esempio);

   ![subs file_select](../img/subs_file_select.png)

6. ora **visionare il lavoro da fare nel suo complesso**, seguendo [le
   istruzioni riportate qui sotto](https://github.com/av-italia/subs/blob/main/doc/translate.md#il-workflow-da-adottare);

7. **una volta chiara la traduzione da effettuare nel suo complesso**,
   puoi cliccare sul pulsante matita per procedere alla modifica del
   file (quello a destra dei bottoni `Raw` e `Blame`);

   ![pencil](../img/pencil.png)

8. fare le modifiche/tradurre (non preoccuparsi del messaggio "You are
   making changes ...")
   
   ![editing](../img/editing.png)

   Se si vuole avere un sommario delle modifiche effettuate spostarsi
   nel tab `Preview changes`;

9. a termine sessione, quando si vuole "salvare", scorrere in basso
   nella pagina, verso la sezione `Propose changes`: cliccare sul
   tasto verde `Propose changes`

	![propose_changes](../img/propose_changes.png)

10. cliccare sul pulsante verde `Create Pull Request`
   
   ![pull_request1](../img/pull_request1.png)

11. cliccare su `Create Pull Request`;

	![pull_request2](../img/pull_request2.png)

12. fine!! 


In seguito a revisione informatica di minima le modifiche saranno
accettate ed integrate: modifiche che impattino su qualsiasi cosa
diversa dalla traduzione (es progressivo sottotitolo, secondi)
saranno verosimilmente rifiutate.
	
Ora, se **occorre finire** il file assegnato, ri-cominciare dal
punto 7 (tener conto che le modifiche in precedenza apportate non
saranno visualizzate, se non sono state nel frattempo
approvate. Tuttavia sono state sottomesse/non perse).

Se viceversa si è **terminato** il proprio file:
* attendere accettazione/merge (comunicata automaticamente via mail);
* *dare comunicazione* in chat che la traduzione è completa
  rispondendo all'assegnazione (per trovarla *cercare il proprio
  username GitHub* nella chat) con **tradotto**

	<img src="../img/tradotto.jpg" alt="tradotto" width="400"/>
 
  Una volta fatto ciò si potrà, compatibilmente con le proprie
  disponibilità **richiedere una nuova assegnazione** mediante
  `@lucailgarb #translate`;

* a questo punto il file verrà preso in carico da uno dei revisori
  (che comunicherà **in revisione**). Il revisore potrà confermare la
  traduzione, anche apportandovi modifiche minori, comunicando
  **completato**; oppure potrà richiedere modifiche ai traduttori
  nello spezzone (mediante commenti) come nel seguente template:

	```
	4
	00:00:51,000 --> 00:01:04,000
	## Inglese da tradurre
	## Inglese da tradurre
	Italiano tradotto
	Italiano tradotto
	## Commento/richiesta del revisore
	## Commento/richiesta del revisore
	```
  
  In questo secondo caso, una volta aggiunti i commenti, il revisore vi
  comunicherà via Telegram la necessità di effettuare le modifiche;
  per farle si seguirà la medesima procedura descritta sopra e al
  termine si comunicherà la cosa al revisore. Il processo andrà avanti
  fino a che la traduzione/revisione linguistica sarà terminata e il
  revisore comunicherà **completato**.

	<img src="../img/completato.jpg" alt="completato" width="400"/>



## Il workflow da adottare

Nell'attività di traduzione **il modo peggiore di procedere**, **da
non adottare**, consiste nel partire a testa bassa con la modifica dei
subs su GitHub, procedendo un sub alla volta, utilizzando Google
Translate e non ascoltando il video.

**Quello che viceversa occorre fare:**

* puntare il proprio browser all'url riportato a inizio file; questo è
  il link all'inizio dello spezzone di propria competenza:

  ![url inizio file](../img/url_inizio_file.png)

* può essere utile **stampare** (su carta riciclata) i sottotitoli,
  per poter avere un supporto utile per appunti/annotazioni ecc;
  
* **ascoltare** l'audio, anche più volte per i punti dubbi,
  **scorrendo visivamente i sottotitoli** in contemporanea. Si
  consiglia di ascoltare anche un pezzo di video precedente e uno
  susseguente, per contesto;

* iniziare ad **abbozzare** punteggiatura, traduzione, e ad evidenziare
  *dubbi*;

* non esitare a **domandare/condividere eventuali dubbi che possono
  essere di utilità per altre/i** nella chat "AV: Traduttori e
  Revisori".  Alcuni suggerimenti su come farlo sono forniti
  [qui](help.md);

* se necessario, su cose specifiche/circoscritte al singolo pezzo (eg
  non cose che possono essere utili anche ad altre/i, le quali sono
  da condividere in chat) si può lasciare un commento al revisore come
  segue:

	  
	```
	3
	00:00:33,000 --> 00:00:49,000
	## Linea 1 in inglese
	## Linea 2 in inglese
	Testo tradotto
	testo tradotto
	## Commento per i revisori
	## commento per i revisori
	
	4
	...
	```

	Da notare che il commento va dopo *2 cancelletti*, come *ultima linea*
	e assicurandosi che dopo vi sia sempre **almeno una linea vuota di
	separazione**.


* una volta che abbiamo una idea compiuta della traduzione da
  effettuare *nella sua interezza* e abbiamo risolto eventuali dubbi,
  possiamo **procedere alla modifica** dei file;
  
* se infine vi sono sub da creare ex novo (es audio completamente
  mancato dal text to speech oppure scritte a video da tradurre)
  aggiungere nel file `zz_UNSUBBED` (nella stessa cartella
  degli altri file del progetto, in fondo) indicando momento di inizio
  (anche i secondi), testo inglese, traduzione italiana, come segue:

	```
	00:00:33
	## Testo inglese
	Testo tradotto in italiano

	...
	```

	Tenere una linea di separazione tra i sub mancanti e porre/mantenere
	in ordine temporale.
	
## Guidelines leggibilità per traduttori

Il file ricevuto è prodotto da un computer/software, ed è ancora "grezzo";
per ottenere dei subs fruibili/professionali/pubblicabili è necessario
adottare vari accorgimenti, che con la pratica diventeranno
automatici.

Tutto questo per suddividerci il lavoro il più possibile, evitare che
ricada sui revisori e velocizzarci.

Per qualsiasi dubbio, come sempre, c'è la chat "AV: Traduttori e
Revisori".

Issue | Regola e/o esempio
------|---------------
Ortografia/Grammatica | Aggiungere punteggiatura, maiuscole ecc, rettificare eventuali errori grammaticali palesi di chi parla
Significatività | Omettere cose come "um" "ah", omettere ripetizioni "Grazie, grazie, grazie mille"
Suoni/Musica         | Descrivere suoni/musica *rilevanti* tra tonde, es "(Porta che scricchiola)" o  "(Musica inquietante)"
Non udibile | Se non si sente/capisce e *sembrerebbe rilevante* porre "[Non udibile]"
Dialoghi | Quando due persone parlano nello stesso sub, ognuno dovrebbe avere una linea per frase, iniziata da un trattino. Porre comunque su più linee; poi, se troppe, il sub verrà in seguito splittato in maniera tale che rimanga leggibile. Ad esempio ...
```
- Hai mai visto immagini del genere?
- No onestamente, mai così.
- Ok, sappi che questa è pratica standard.
- Ah.
```


