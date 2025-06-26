import scala.collection.mutable.HashSet
import scala.compiletime.ops.double
    

@main def rabinKarpMultiPattern(): Unit = 
    // modulo Value
    val mod: Long = 1000000007L // sehr lange zahl die zufaellig eine Primzahl ist lul 
    val base: Int = 31 // Primzahl zur eindeutigen gewichtung der Hashwerte

    val suchmuster = List("abc", "def", "ghi") // Suchmuster
    val text = "abcdefghijklmnghiopdefqrsabc"
    val m = suchmuster.head.length // Setzt den ersten Eintrag als feste laenge von m

    // Umwandeln der Zeichen in Zahlenwerte (a=1, b=2 usw.)
    def charValue(c: Char): Int = c - 'a' + 1


    // Hashfunktion 
    def Hash(s: String): Long = 
        var hash = 0L
        for i <- 0 to s.length - 1 do
            // wir berechnen die Exponentialwerte aus
            val expow = math.pow(base, s.length - i - 1).toLong
            hash = (hash + charValue(s(i)) * expow) % mod
        hash

    // Berechnung des Base Hashes: base^(m-1) fuer den Rolling Hash
    val basePower: Long = math.pow(base, m-1).toLong % mod


    // 1. Muster Hashes berechnen
    val musterHash = HashSet[Long]() // Initialisiere die Datenstruktur HashSet
    for muster <- suchmuster do
        musterHash.add(Hash(muster)) // fuer jeden Eintrag in der Liste suchmuster berechnen wir den Hash und speichern ihn im Hashset

    // 2. Rolling Hashe fuer alle Fenster berechnen
    var hash = Hash(text.substring(0, m))

    // Loop fuer den Rolling Hash
    var i = 0
    while i <= text.length - m do
        // Pruefen ob der Hash passt
        if musterHash.contains(hash) then
            val fenster = text.substring(i, i + m) // setzen des neuen Fensters
            if suchmuster.contains(fenster) then 
                println(s"Treffer bei Index $i: $fenster")
        
        // Verschiebung des Fensterbereichs fuer den Rolling Hash
        if i + m < text.length then 
            val oldChar = charValue(text(i))
            val newChar = charValue(text(i+m))

            // Rolling Hash - entferne das erste Zeichen, mal der Base, addiere neues Zeichen
            hash = (hash - oldChar * basePower % mod + mod) % mod
            hash = (hash * base + newChar) % mod

        i += 1
    
    println("Finished: Kein Muster gefunden.")