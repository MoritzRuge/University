#Schreibe Sie ein Python-Programm, das drei ganze Zahlne erhält, und genau dann True ausgibt, wenn die Zahlen alle gleich sind.

# Funktion die überprüft ob alle Zahlen gleich sind
def zahlen_alle_gleich(a, b, c):
    return a==b and a==c and b==c #retuned nur dann true wenn alle gleich sind

# User input der drei Zahlen
zahl1 = int(input("Bitte die erste Zahl eingeben: "))
zahl2 = int(input("Bitte die zweite Zahl eingeben: "))
zahl3 = int(input("Bitte die dritte Zahl eingeben: "))

# Ausgabe des Ergebnis
print(zahlen_alle_gleich(zahl1, zahl2, zahl3))
