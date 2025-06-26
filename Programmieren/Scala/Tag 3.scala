/*
Aufgabe: Fakultät berechnen (rekursiv)
Die Fakultät einer Zahl n (geschrieben n!) ist definiert als:
    0! = 1
    n! = n × (n-1)! für n > 0

Schreibe eine rekursive Funktion fakultaet(n: Int): Int, die die Fakultät einer Zahl berechnet.
    Nutze keine Schleifen (for, while)!
    Die Funktion soll rekursiv arbeiten.
    Du kannst am Ende eine main-Funktion schreiben, die z. B. fakultaet(5) aufruft und das Ergebnis ausgibt.
*/

@main def day3(): Unit =

    val zahl = 5

    def fakultät(n: Int): Int = 
        if n == 0 then  1
        else n * fakultät(n-1)


    val result = fakultät(zahl)
    println(result)