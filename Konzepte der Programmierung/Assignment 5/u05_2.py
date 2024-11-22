#fibonacci zahl
#a) Implementieren Sie die rekursive Definition der Fibonacci-Zahl direkt in Python

cache = {}

def Fibonacci(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    
    if n in cache:
        return cache[n]
    
    result = Fibonacci( n - 1 ) + Fibonacci(n - 2)
    cache[n] = result
    return result


print(Fibonacci(35))