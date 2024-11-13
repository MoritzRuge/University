#Aufgabe 1
"""
1. Zufallszahlen erzeugen
2. Überprüfen, ob alle Zahlen vorgekommen sind (im Set, keine doppelten Werte)
3. Versuche zählen, mit counter bis alle Zahlen gezogen wurden
4. Skalierung, eingabe wie oft der Vorgang wiederholt werden soll
5. Ergebnisse darstellen
"""

import random
import numpy as np

def experiment(n):
    drawn_numbers = set()
    counter = 0
    while len(drawn_numbers) < n:
        number = random.randint(1, n)
        drawn_numbers.add(number)
        counter +=1
    return counter

def run_experiment(scope, limit=100):
    result = [experiment(scope) for _ in range(limit)]
    min_result = min(result)
    max_result = max(result)
    average_result = np.mean(result)
    return min_result, max_result, average_result


for n in [10, 100, 1000]:
    min_result, max_result, average_result = run_experiment(n)
    predicted_result = n * sum(1/k for k in range(1, n+1))
    print(f"n={n}")
    print(f"Minimum: {min_result}")
    print(f"Maximum: {max_result}")
    print(f"Average: {average_result:.0f}")
    print(f"Predicted: {predicted_result:.0f}")


