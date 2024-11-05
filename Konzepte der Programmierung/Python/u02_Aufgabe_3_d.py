#Schreiben Sie ein Python-Programm, das drei ganze Zahlen erhält, und ausgibt, um wie viele verschiedene Zahlen es sich handelt.

# Function which looks for different numbers
def wieviel_verschiedene_zahlen(a,b,c): # takes 3 input variables
    zahlen_set = {a,b,c} # we crate a Set which does not take the same input twice
    return len(zahlen_set) # retun the length of the set, if all numbers are equal retun 1, if not retun 3

# prompt user for input
zahl1 = int(input("Bitte geben Sie die erste Zahl ein: "))
zahl2 = int(input("Bitte geben Sie die zweite Zahl ein: "))
zahl3 = int(input("Bitte geben Sie die dritte Zahl ein: "))

# print the result
print(wieviel_verschiedene_zahlen(zahl1,zahl2,zahl3))

