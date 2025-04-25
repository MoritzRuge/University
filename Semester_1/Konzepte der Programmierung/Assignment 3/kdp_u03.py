n = 7 # anzahl zeilen
for i in range(1, n + 1): # erstellt die anzahl der Zeilen über die wir Itterieren
    space = " " # variable leeres feld auszugeben
    print(space * (n - i), end="") # für jeden durchgang wird vor der Zahl ein leeres Feld ausgegeben
    for j in range(1, i + 1): # Ausgabe der rechten Zahlenhälfte
        print(j, end="")
    for k in range(i - 1, 0, -1): # Ausgabe der linken Zahlenhälfte
        print(k, end="")

    print("") # print der neuen Zeile
