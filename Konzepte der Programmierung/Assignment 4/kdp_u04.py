#Aufgabe 1
"""
1. Zufallszahlen erzeugen
2. Überprüfen, ob alle Zahlen vorgekommen sind (im Set, keine doppelten Werte)
3. Versuche zählen, mit counter bis alle Zahlen gezogen wurden
4. Skalierung, eingabe wie oft der Vorgang wiederholt werden soll
5. Ergebnisse darstellen
"""

import random

# function which should count all random numbers and store them in a set of numbers
def numberStore():
    numberset = set(())
    counter = 0
    for i in range(10):
        n = random.randint(1, 10)
        numberset.add(n)
        counter += 1

    print(numberset , " and Counter:" ,counter)


numberStore()