2a)

steps of topoSort:

1\. visited:{/}, topoorder:{/} start at 1.

&nbsp;	visited:{1}, topoorder:{/}

&nbsp;	1 has outgoingedge too: 3 -> dfs(3,t)

1.2

&nbsp;	visited:{1,3}, topoorder:{/}

&nbsp;	3 has outgoingedges too: 2, 5 -> 2 Comes before 5 -> dfs(2,t)

1.3 	

&nbsp;	visited:{1,3,2}, topoorder:{/}

&nbsp;	2 has outgoingedges too: 5 -> dfs(5,t)

1.4

&nbsp;	visited:{1,3,2,5}, topoorder:{/}

&nbsp;	5 has no outgoingedges: -> push(5) -> traceback 2: push(2) -> traceback 3: 5 in visited / found push(3) -> traceback 1: push(1)

2\. visited:{1,3,2,5}, topoorder:{1,3,2,5}

&nbsp;	2 in visited / found

3\. visited:{1,3,2,5}, topoorder:{1,3,2,5}

&nbsp;	3 in visited / found

4\. visited:{1,3,2,5,4}, topoorder:{4,1,3,2,5}

&nbsp;	4 has outgoingedges too: 5 -> 5 in visited / found -> push(4)

5\. visited:{1,3,2,5,4}, topoorder:{4,1,3,2,5}

&nbsp;	5 in visited / found

6\. visited:{1,3,2,5,4,6}, topoorder:{4,1,3,2,5}

&nbsp;	6 has outgoingedges too: 5 -> 5 in visited / found -> push(6)

topoorder:{6,4,1,3,2,5}

all nodes / verticies are found. The topological order is derived from poping all Elements from the stack LIFO -> 6,4,1,3,2,5



2b)

Annahme: Es existiert ein Knoten **w** mit einer ausgehenden Kante **i** zu einem führen Knoten **v**, welcher keine ausgehende Kante zu **w** hat, in einer topologischen Sortierung.



In der Tiefensuche wird an einem Knoten gestartet und es wird solange rekursiv ein Pfad verfolgt, bis ein Knoten keine ausgehenden Kanten mehr hat. Dabei werden all Knoten als gefunden markiert und mittels rekursiven Backtracking auf den Stack, der die topologische Ordnung speichert, gepushed. sollte ein anderer Knoten eine ausgehende Kante zu einem bereits gefunden und gepushten Knoten haben, so wird dieser in der Tiefensuche nicht erneut betrachtet bzw. mittels dfs() besucht. Dies gilt für die dfs() Aufrufe von Nachbarn in der dfs Funktion und den dfs() Aufruf in der topoSort() Funktion 

```

if !w.found then

&nbsp;  dfs(w, topoOrder)

```

```

if !v.found do

&nbsp;  dfs(v, topoOrder)



``` 

Wurde ein Knoten bereits gefunden, werden diese Ausdrücke für diesen Knoten immer zu false evaluieren und daher, wird kann dieser nicht erneut Teil eines Pfades werden.

Wenn der Knoten **w** eine ausgehende Kante zu einem früheren Knoten **v** hat, dann gilt einer von zwei Fällen in einer topologischen Sortierung:

1. **Fall:**

Die Knoten **w** und **v** sind beide Teil eines Längeren Pfades vom einem anderen Knoten **u.** Dabei kann zuerst **v**  besucht werden, wodurch der Pfad von **w** zu **v** nicht verfolgt oder zuerst wird der längere Pfad von **w** verfolgt, wodurch der Pfad von **w** über **v** teil der topologischen Ordnung wird und der Pfad des anderen führen Knotens zu **v** nicht verfolgt wird. Beispiel siehe Graph von 2a)

**2. Fall:**

Im gegeben Graph G liegt ein Kreis vor. Dadurch würde der Graph allerdings nicht mehr die Voraussetzungen für die Sortierung erfüllen und wäre ungültig.



Zusammenfassung:

In einem gültigen Graphen ist es nicht möglich, dass eine Kante von einem späteren Knoten zu einem früheren Knoten, welcher bereits gefunden wurde, in der topologischen Sortierung auftaucht.

