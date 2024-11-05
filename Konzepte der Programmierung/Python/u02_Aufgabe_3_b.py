#Schreibe ein Python programm, das drei ganze Zahlen erhält, und genau dann True ausgibt, wenn die Zahlen paarweise verschieden sind.

def sind_paarweise_verschieden(a, b, c):
    return a != b and a != c and b != c # returned nur dann True wenn alle vergleiche True sind

# User prompt zur Zahleneingabe
zahl1 = int(input("Geben Sie die erste Zahl ein: "))
zahl2 = int(input("Geben Sie die zweite Zahl ein: "))
zahl3 = int(input("Geben Sie die dritte Zahl ein: "))

# Ausgabe, ob die Zahlen paarweise verschieden sind
print(sind_paarweise_verschieden(zahl1, zahl2, zahl3))


