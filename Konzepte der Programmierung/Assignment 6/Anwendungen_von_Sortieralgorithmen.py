"""
- n mehlsäcke mit unterschiedlichen Gewicht
- schauen ob sich die Mehlsäcke nur um 10 Gramm unterscheiden
- Mehlsäcke können als eine Liste von Zahlen modellieren
"""

def vergleich(mehlsäcke):
    # Vergleiche 2 Mehlsäcke und finde herraus welche säcke sich um 10 gramm unterscheiden
    ergebnisse = []
    n = len(mehlsäcke)
    
    mehlsäcke.sort() # python sortierfunktion 

    for i in range(len(mehlsäcke) - 1):
        differenz = mehlsäcke[i + 1] - mehlsäcke[i]
        if differenz <= 10:
            return (mehlsäcke[i], mehlsäcke[i + 1])

    return None

# Mehlsäcke in Gramm als eine Liste
mehlsäcke = [10, 40, 60, 90, 20]


ergebnis = vergleich(mehlsäcke)
for eintrag in ergebnis:
    
    if ergebnis:
        print(f"Mehlsack {ergebnis[0]} und {ergebnis[1]} unterscheiden sich um 10 Gram")
    else:
        print("Keine passendes Paar gefunden")



"""
    for item in range(0, n-2, 2):
        if mehlsäcke[item] < mehlsäcke[item+1]:
            differenz = mehlsäcke[item+1] - mehlsäcke[item]
            if differenz > 10:
                ergebnisse.append(f"Mehlsack{item} ist mit einen Wert von {differenz} kleiner gegenüber Mehlsack{item+1}")
            else:
                ergebnisse.append("ungefähr gleich schwer")
        elif mehlsäcke[item] > mehlsäcke[item+1]:
            differenz = mehlsäcke[item] - mehlsäcke[item+1]
            if differenz > 10:
                ergebnisse.append(f"Mehlsack{item} ist mit einen Wert von {differenz} größer gegenüber Mehlsack{item+1}")
            else:
                ergebnisse.append("ungefähr gleich schwer")
    return ergebnisse
"""
