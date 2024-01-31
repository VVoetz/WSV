# Lectures en Lesroosters
De case lectures en lesroosters is een variant van het university timescheduling problem, waar er geprobeerd wordt een zo goed mogelijk rooster te maken. De kwaliteit van een rooster wordt bepaald door de hard en soft constraints rondom de variablen van het probleem.
Dit is een project voor het vak Algoritmen en Heuristieken van de Minor Programmeren van de UvA.

### Hard constraints
- Elke benodigde activiteit moet ingeroosterd worden op een zaalslot (een voorbeeld van een activiteit is: lineaire algebra, hoorcollege 1)
- Elke student moet ingedeeld worden in de benodigde vak activiteiten van de vakken waarvoor ze staan ingeschreven
- Er mogen niet meerdere activiteiten worden ingeroosterd op één zaalslot
- Er mag geen rooster zijn waar een student 3 tussenuren heeft

### Soft constraints
- Een student heeft zo min mogelijk activiteiten op hetzelfde tijdstip
- Een student heeft zo min mogelijk tussenuren
- Iedereen past in de zaal waarin ze zijn ingeroosterd
- Er zijn zo min mogelijk activiteiten geroosterd op het 5e tijdslot (van 17:00 tot 19:00)
- Iedereen past in de activiteit waarin ze zijn ingeroosterd

# Installatie
- 'git clone https://github.com/VVoetz/WSV/'
- 'pip3 install -r requirements.txt'

# Tutorial
-- TODO --
# Algoritmen

De algoritmen die worden getest om dit probleem op te lossen zijn
- random
- greedy
- hillclimber
- simulated annealing
- tabu search

## Random
Het random algoritme maakt een compleet random rooster aan door alle activiteiten aan een lijst toe te voegen, om vervolgens dummy-activiteiten toe te voegen zodat alle zaalsloten gebruikt kunnen worden. De lijst wordt geshufflet en de activiteiten worden vervolgens in het eerste vrije tijdslot van de eerste room ingepland.
Daarna worden alle studenten aan alle hoorcolleges toegevoegd voor de vakken die ze volgen. Voor de werkcolleges en practica, waarvan er soms meerderen zijn omdat er een max aantal studenten kan zijn voor die activiteiten, worden studenten random ingeschreven in één van de verschillende activiteiten. Mocht deze activiteit al vol zitten (hard constraint), dan zal de student aan een willekeurige andere activiteit worden toegevoegd.
Het is mogelijk dat de uitkomst van dit algoritme niet voldoet aan de hard constraints. In dat geval zal het totaal aantal maluspunten boven 1000000 liggen.

## Greedy
Bij het greedy algoritme worden er activiteiten op basis van het verwachtte aantal studenten dat in deze activiteit zal komen te zitten gesorteerd en daarna aan een zaal toegevoegd. Het zal per activiteit de kleinste zaal zoeken die groot genoeg is om alle verwachtte studenten te huisvesten. Het algoritme zal het eerst mogelijke tijdslot kiezen dat er in die zaal nog over is. Mocht er geen zaal groot genoeg zijn dan zal de zaal met de hoogste capaciteit (mits deze nog open tijdsloten hebben) gekozen worden. Daarna worden voor alle hoorcolleges alle studenten toegevoegd die het vak volgen. Voor de werkcolleges en practica worden per vak en daarna per activiteit alle studenten toegevoegd. Eerst wordt gekeken hoeveel er van die twee type activiteiten zijn. Daarna worden de studenten die voor dat vak staan ingeschreven gesorteerd op basis van hoeveel vakken zij volgen. De studenten met de meeste vakken zullen als eerst toegevoegd worden aan de activiteit die de minste maluspunten oplevert, mits het maximale aantal studenten in de desbetreffende activiteit niet is bereikt.
Bij dit algoritme is bij de initialisatie het vijfde tijslot van zaal C0.110 weggehaald, om hem weer beschikbaar te maken nadat het algoritme klaar is. Zo worden het aantal maluspunten die het 5e tijdslot oplevert geminimaliseert. Ook zou dit algoritme anders altijd een onjuist rooster creeëren, waarin 3 tussenuren achter elkaar plaatsvinden.

## hillclimber
Bij het hillclimber algoritme worden alle activiteiten en daarna studenten random ingeroosterd. Er wordt wél rekening gehouden dat er niet te veel studenten in een werkcollege of practicum zitten, er wordt geen rekening gehouden met het feit dat studenten wellicht 3 tussenuren achter elkaar hebben (en dus >1000000 maluspunten krijgen). De implementatie is iets anders dan in het eerder gecreëerde random algoritme (random_algo.py). Het resultaat is echter gelijk.
Daarna zal het hillclimber algoritme voor een N aantal iteraties per iteratie zowel twee random gekozen activiteiten swappen als 2 random gekozen studenten tussen activiteiten in een vak. Het is ook mogelijk dat een activiteit swapt met een leeg zaalslot. Ook is het mogelijk dat een student wordt verplaatst naar een andere activiteit zonder dat er een student de andere kant op beweegt. De kans dat er een verplaatsing plaatsvindt in plaats van een swap is gebaseerd op de hoeveelheid lege zaalsloten (voor activiteiten) en de capaciteit van de activiteiten (voor studenten). Bij beide swaps wordt gekeken of de verandering een positieve invloed heeft op het totaal aantal maluspunten. Als de verandering het aantal maluspunten verminderd en ook als het gelijk blijft, dan zal de verandering geaccepteerd worden. Anders wordt de verandering ongedaan gemaakt. Dit gaat door totdat er voor een X aantal iteraties geen verandering is geweest in de hoeveelheid maluspunten. Bij dat van tevoren aangegeven getal zal het algoritme stoppen.
## Simulated annealing
Bij het simulated-annealing algoritme zijn er verschillende manieren om een initiële oplossing te verkrijgen. Mocht het data meekrijgen waarin er al een compleet rooster is gemaakt, dan zal het daarop verdergaan. Als er nog niks is ingeroosterd binnen de data, dan zal het eerst een random oplossing genereren om vervolgens aan de slag te gaan.
Het simulated-annealing algoritme zal netals het hillclimber algoritme per iteratie zowel een verandering van activiteiten als studenten plaatsvinden. Bij dit algoritme is het echter ook mogelijk dat een activiteit wordt verplaatst naar een leeg zaalslot en dat er een student wordt verplaatst naar een andere activiteit. Ook is er een 10% kans per iteratie dat 3 activiteiten tegelijk worden verwisseld met elkaar. Bij alle geteste veranderingen wordt gekeken naar het aantal maluspunten + 'neppe' maluspunten. De neppe maluspunten zijn punten die door de heuristieken kunnen worden gegeven om het algoritme meer te kunnen sturen. Als er een verbetering is of als het aantal (neppe) maluspunten gelijk blijft dan wordt de verandering geaccepteerd. Als er meer maluspunten zijn dan voor de verandering zal met behulp van de huidige temperatuur, een coëfficient en het daadwerkelijke verschil in maluspunten de kans worden berekent dat deze 'slechte' verandering alsnog wordt goedgekeurd. Dit algoritme zal doorgaan totdat er een bepaald aantal iteraties géén verandering is geweest in maluspunten óf als het maximale aantal iteraties is bereikt.

## Tabu search
Ook bij het tabu search algoritme zijn er meerdere mogelijke manieren om een initiële oplossing te krijgen. Als de optie create\_initial\_solution True is, dan maakt het algoritme eerst een random indeling van de activiteiten en studenten. Als die optie False is, dan gaat het algoritme door met de oplossing die wordt meegegeven. Tabu search zoekt voor een N aantal iteraties naar een X aantal buren. Deze buren zijn variaties van de vorige iteratie en bevat activiteit swaps, activiteit moves, studenten swaps en studenten moves. Tijdens het verkrijgen vnan de buren, wordt ook het aantal maluspunten verschil van die buren berekend. Daarna gaat het algoritme elke buur af en kiest de beste buur uit. Dit kan dus ook voor een verslechtering zorgen, als er geen betere buren gevonden worden. Als uiteindelijk de buur is gekozen, wordt deze verandering toegevoegd aan een tabu_lijst, waardoor het voor een Y aantal iteraties diezelfde swap niet mag maken. Het algoritme stopt wanneer de tijd om is, wanneer het een bepaald aantal iteraties geen nieuwe beste score heeft gevonden of wanneer het maximaal aantal iteraties is bereikt.

## Auteurs
- Victor Germans
- Sunshine Landvreugd
- Wouter Bentvelzen
