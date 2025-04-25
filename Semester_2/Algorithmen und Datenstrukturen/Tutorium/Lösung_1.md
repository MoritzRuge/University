Aufgabe 1: Binäre Heaps und binäre Suchäume I
	Nennen Sie die Eigenschaften eines binären Suchbaums und die Eigenschaften eines binären Heaps. Was sind Gemeinsamkeiten, was sind Unterschiede?

*Binäre Suchbäume*: 
- Wenn der Suchbaum leer ist, dann ist er ein binärer Suchbaum
- Wenn wir zwei Teilbäume haben Tl und Tr, sind Tl und Tr binäre Suchbäume, wenn k die Wurzel von


## Binary Heaps
- min-heap T ist ein binärer Baum der folgende Eigeschaften erfüllt:
	- (i) Ein Binärer Heap ist geordnet, d.h. das kleinste Element ist in der Wurzel gespeichert und alle andern Knoten sind gleich klein oder kleiner als dessen Kinder
	- (ii) h ist die höhe des Baumes T. Die verschiedenen Leves des Baums sind immer komplett gefüllt mit Knoten bzw. Blättern und in level h sind die Blätter links Orientiert
	- max-heap ist umgekehrt zu (i)
	- ein leerer Baum wäre auch Suchbaum
- Binäre Suchbäume
	- Knoten hat immer zwei Kinder
	- Von der Wurzel k aus, 

Aufgabe 3:
- Beste Laufzeit O(n), weil wir jeden Konten mindestens einmal überprüfen müssen um sicher zu sein, das der Suchbaum Korrekt ist.
- Algorithmus von Tiefensuche anschauen
- wir speichern zwei werte, für die Obere Grenze und die Untere(- Unendlich und + Unendlich
- dann vergleichen wir die Wurzel mit den Kindern und setzten die grenzen neu
	- Root 10 , l = 5, r=100
	- stimmt so, wir gehen in den linken TEilbaum mit den Grenzen -unendlich und als max = 10 
	- bis wir die Grenzen soweit eingegerenz haben, das ein fehler auftritt, weil der Wert nicht passt, oder weil wir kein Teilbaum/Knoten mehr haben und der Suchbaum korrekt ist.
