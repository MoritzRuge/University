import scala.collection.mutable.HashSet
import scala.compiletime.ops.double

@main def rabinKarpMultiPattern(): Unit = 
    // RabinKarp Values
    val mod: Long = 1000000007L // sehr lange zahl die zufaellig eine Primzahl ist lul 
    val base: Int = 31 // Primzahl zur eindeutigen gewichtung der Hashwerte

    // Importiert die Text Datei des Buches, nachdem try succseded, close file
    val source = scala.io.Source.fromFile("Sense and Sensibility.txt")
    val text = try source.mkString finally source.close()
    val cleanText = text.toLowerCase().replaceAll("[^a-z]", "") // Entfernt Satzzeichen und Leerzeichen

    // Muster vorbereiten
    val musterA = List("sense")
    val musterB = List("sensibility")
    val musterC = List("sensible")

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

    // Rolling hash und zaehlen der Woerter
    def rollingMatchCount(text: String, muster: List[String]): Int =
        if muster.isEmpty then return 0
        val m = muster.head.length // Setzt den ersten Eintrag als feste laenge von m
        val musterSet = muster.toSet // Wandeln muster: List zu muster: Set um, um O(1) laufzeit zu kriegen
        val musterHashes = HashSet.from(muster.map(Hash)) // Bauen ein HashSet aus musters

        // Berechnung des Base Hashes: base^(m-1) fuer den Rolling Hash
        val basePower: Long = math.pow(base, m-1).toLong % mod
        var hash = Hash(text.take(m))
        var count = 0
        var i = 0

        // Rolling hash loop
        while i <= text.length - m do
            if musterHashes.contains(hash) then 
                val fenster = text.substring(i, i + m) // setzt das Fenster
                if musterSet.contains(fenster) then  // Wenn Fenster in Set vorhanden count +1
                    count += 1

            // Rolling hash updaten entferne alten Char und fuege neuen ein
            if i + m < text.length then 
                val oldChar = charValue(text(i))
                val newChar = charValue(text(i + m))
                hash = (hash - oldChar * basePower % mod + mod) % mod
                hash = (hash * base + newChar) % mod
            i += 1

        count // return value

    // Funktionsaufruf und Zaehlung der Woerter
    val countSense = rollingMatchCount(cleanText, musterA)
    val countSensibility = rollingMatchCount(cleanText, musterB)
    val countSensible = rollingMatchCount(cleanText, musterC)
    val countOther = countSensible + countSensibility

    println(s"sense kommt $countSense mal vor.")
    println(s"sensible kommt $countSensible mal vor.")
    println(s"Sensibility kommt $countSensibility mal vor.")
    println(s"sensibility und sensible kommen $countOther mal vor")

    if countSense > countOther then
        println("sense kommt oefter vor")
    else if countSense < countOther then
        println("sensibility/sensible kommt oefter vor")
    else
        println("Beide Muster kommen gleich oft vor.")