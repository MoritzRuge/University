n = 7 # anzahl zeilen
for i in range(1, n + 1):  #Schleife die n mal durchläuft
    space = " " # Variable um ein leeres Feld zu zeichnen
    print(space * (n - i), end="") # dekrement um den Betrag von i
    for j in range(1, i + 1): # Ausgabe der aufsteigenden Zahlenreihe
        print(j, end="")
    for k in range(i - 1, 0, -1): # Ausgabe der absteigenden Zahlenreihe
        print(k, end="")

    print("") #Zeilenumbruch
