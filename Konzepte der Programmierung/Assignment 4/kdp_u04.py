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
        number_key, number_value = count_number(number)
        counter +=1
    return counter, number_key, number_value

def run_experiment(scope, limit=100):
    result, number_key, number_value = [experiment(scope) for _ in range(limit)]
    min_result = min(result)
    max_result = max(result)
    average_result = np.mean(result)
    return min_result, max_result, average_result, number_key, number_value


def count_number(number):
    number_dictionary = dict()
    number_value = 0
    number_key = 0
    
    # if number is not in dic , add it to the dictionary with value 1
    if number not in number_dictionary:
        number_dictionary = {number: 1}
    # if number is present, update the key value to plus 1
    else:
        dic_update = {number: number_dictionary[number].get() + 1}
        number_dictionary.update(dic_update)

    # loop through the dic to get the highest value
    for _ in number_dictionary:
        if number_dictionary[number] > number_value:
            number_value = number_dictionary[number]
            number_key = number


    # return the highest number and the count
    return number_key, number_value


def main():
    for n in [10, 100, 1000]:
        min_result, max_result, average_result, number_key, number_value = run_experiment(n)
        predicted_result = n * sum(1/k for k in range(1, n+1))
        print(f"n={n}")
        print(f"Minimum: {min_result}")
        print(f"Maximum: {max_result}")
        print(f"Average: {average_result:.0f}")
        print(f"Predicted: {predicted_result:.0f}")
        print(f"Highest number is {number_key} with {number_value}x pick")


if __name__ == "__main__":
    main()