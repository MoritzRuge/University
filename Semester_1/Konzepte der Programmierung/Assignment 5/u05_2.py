#fibonacci zahl
#a) Implementieren Sie die rekursive Definition der Fibonacci-Zahl direkt in Python
#c) Modifiziere das Programm so, dass es bekannte Ergebnisse 

# c) cache speicher
cache = {}

def Fibonacci(n):
    # Basisfälle / Stopbedingung
    if n == 1:
        return 1
    elif n == 0:
        return 0
    
    # c) ruft n aus cache ab
    if n in cache:
        return cache[n]
    
    # Rekursive abrufe von n-1 und n-2
    result = Fibonacci( n - 1 ) + Fibonacci(n - 2)
    cache[n] = result # c) speichert den wert von result in cache mit position n
    return result


print(Fibonacci(35))