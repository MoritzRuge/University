#Rekursionsdrill
#a) Schreiben Sie eine rekursive Funktion, die das Produkt einer Liste von Zahlen berechnet.
"""def Lenght(list):
    if list == []:
        result = 0
    else:
        result = 1 + Lenght(list[1:])
    return result

a = [1,2,3,4,5,6,7,8,9,10]

print(Lenght(a))
"""
#b) Schreiben Sie iene rekursive Funktion, die das Produkt einer Liste von Zahlen berechnet.
"""
def Product(list):
    if list == []:
        result = 1
    else:
        result = list[0] * Product(list[1:])

    return result

a = [2,5,3,10]

print(Product(a))
"""
#c) Schreiben Sie eine rekursive Funktion, die das Minimum einer Liste von Zahlen berechnet.

def min_list(list):
    if min_list == []:
        result = 0
    else:
        

        
    return result

a = [5,4,7,9,2]

print(min_list(a))