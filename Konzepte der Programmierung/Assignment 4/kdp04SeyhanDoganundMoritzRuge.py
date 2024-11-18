import random #Seyhan Dogan, Moritz Ruge
import statistics
from collections import Counter

def experimentZahlen(n, k=100):
    Zahlen = []
    haeufigste_zahlen = []
    haeufigkeiten = []

    for i in range(k):
        done = set()
        counter = 0
        frequency = Counter()  # zähler für häufigkeit der Gzogenen zahlen

        while len(done) < n:  # solange nicht jede zahl einmal gefunden wurde
            randnumber = random.randint(1, n+1)  # n+1, da randint obere grenze nicht miteinschließt!!!
            done.add(randnumber)
            frequency[randnumber] += 1
            counter += 1

        Zahlen.append(counter)
        # häufigste zahl und deren häufigkeit bestimmen für 1b)
        haeufigste_zahl, haeufigkeit = frequency.most_common(1)[0]
        haeufigste_zahlen.append(haeufigste_zahl)
        haeufigkeiten.append(haeufigkeit)

    minimum = min(Zahlen)
    maximum = max(Zahlen)
    durchschnitt = statistics.mean(Zahlen)
    haeufigste_zahl = statistics.mode(haeufigste_zahlen)
    haeufigkeit_der_haeufigsten_zahl = statistics.mode(haeufigkeiten)

    return minimum, maximum, durchschnitt, haeufigste_zahl, haeufigkeit_der_haeufigsten_zahl

def harmonischnummerding(n):
    h = n * sum(1/i for i in range(1, n+1))
    return h

versuche = [10, 100, 1000]

for n in versuche:  # für jeweils 10, 100 und 1000
    minimum, maximum, durchschnitt, haeufigste_zahl, haeufigkeit = experimentZahlen(n)
    erwartung = harmonischnummerding(n)
    print(f"\nFür n = {n}:")
    print(f"Minimum: {minimum}")
    print(f"Maximum: {maximum}")
    print(f"Durchschnittliche Anzahl der Ziehungen: {durchschnitt:.2f}")
    print(f"Erwartungswert (Harmonische Zahl): {erwartung:.2f}")
    print(f"Häufigste gezogene Zahl: {haeufigste_zahl} (Häufigkeit: {haeufigkeit})")
 # gibt für jedes n durchschnitt, minimum und maximum an:
"""
n = 10
n Minimum: <built-in function min>
n Maximum: <built-in function max>
n Durchschnitt: 22.82
Erwartungswert: 29.29
n = 100
n Minimum: <built-in function min>
n Maximum: <built-in function max>
n Durchschnitt: 431.48
Erwartungswert: 518.74
n = 1000
n Minimum: <built-in function min>
n Maximum: <built-in function max>
n Durchschnitt: 6560.84
Erwartungswert: 7485.47
"""
#Nr.2 a)
#die Idee hinter der Formel ist durch iteration näher an wurzel a zu kommen 
# indem man den durchschnitt von xn-1 und a/xn-1 rechnet. Mit jeder iteration wird es dabei genauer
#b)
def wurzel(a, toleranz=1e-10,versuche= 10000):
 xn = 1.0
 if a == 0:
  print("Wuzrel von 0 ist 0")
  return 
 for i in range(versuche):
  xkonvergiert = 0.5*(xn +(a/xn))# die formel
  if abs(xkonvergiert -xn) < toleranz: # toleranz bestimmt, wann es "nah genug" ist
     print(f"Wurzel von {a} ist {xkonvergiert}.")
     return xkonvergiert
  xn = xkonvergiert #formel wird auf das neue x angewendet in nächster iteration!
 print(f"Wurzel von {a} ist {xkonvergiert}.")
 return
wurzel(100)
wurzel(200)
wurzel(5)
# bei a= 100 kam 10, a= 200 kam 14.142135623730951, bei a=5 kam 2.23606797749979
#c)
#basiert auf binary search

def wurzelbinär(a, tol=1e-10, max_iter=1000):
    # Intervall
    x = 1.0
    y = a
    for i in range(max_iter):
        z = (x + y) / 2  # berechne mittelwert
        # überprüfe, ob z^2 nahe genug ist
        if abs(z**2 - a) < tol:
            print(f"Die Wurzel von {a} ist ungefähr {z}")
            return z
        
        if z**2 > a:
            y = z  # quadrat zu groß, Intervall kleiner machen für y
        else:
            x = z  # quadrat zu klein intervall nachlinks verschieben
    print(f"Die Wurzel von {a} ist ungefähr {z}")
    return z 
wurzelbinär(100)
wurzelbinär(200)
wurzelbinär(5)
# bei a= 100 kam 10.00000000000307, a= 200 kam 14.142135623728109, bei a=5 kam 2.2360679775010794
# die erste funktion aus a) hat eine bessere Laufzeit und ist generell genau genug, daher bevorzuge ich diese auch

#Nr.3
"""
a = [1, 3, (4, 2)] gültig, liste von 1,3 und tupel mit 4 und 2

b = (a, a, [1, 5, 4, 3]) gültig, b ist tupel mit element a a und einer liste die 1 5 4 3 enthält

print(b[1][2]) gültig, von b wird erstes element, die liste a gewählt, bei a ist an index 2 das tupel (4,2)

b[1][2] = "wer" versucht den tupel aus a zu verändern, aber tupel sind immutable also kommt ein fehler

print(b) printet b, also ([1, 3, (4, 2)],[1, 3, (4, 2)], [1, 5, 4, 3]) aber da vorherige zeile fehler ist wird sie nicht ausgeführt (werde ich für künftige zeilen ignorieren)

a[2][1] von dem tupel an index 2 in a das element an index 1 also 2, ist gültig  

a[2][1] = "wann" wie vorher, tupel sind immutable, es kommt ein fehler

print(b) vorherige anweisung führt zu einem fehler, würde aber sonst ([1, 3, (4, 2)],[1, 3, (4, 2)], [1, 5, 4, 3]) ausgeben

b[2][1] vom tupel b das element an index 2, also die liste und dort das element am index 1 also 5 zürückgeben, gültig

b[2][1] = ["wo", "wie"] gültig, da eine Liste in einem tupel verändert wird, es würde [1, ["wo", "wie"],4,3] sein

print(b) b wäre jz ([1,3,(4,2)], [1,3,(4,2)], [1, ["wo", "wie"],4,3])

b[2] = [2, 4] die liste in b an index 2 wird durch [2,4] ersetzt.

print(b) = ([1,3,(4,2)], [1,3,(4,2)], [2,4])

a = "warum" a wird zum string "warum" in b ist aber jz eine kopie von a, also keine auswirkung auf b

print(b) b ist immernoch ([1,3,(4,2)], [1,3,(4,2)], [2,4])
"""
 
 