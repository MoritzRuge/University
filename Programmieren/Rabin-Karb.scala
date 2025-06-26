// Hashfunktion (z. B. Rolling Hash mit Modulo p)
def hash(s: String): Int = 
    // Dictionary für Sum also die Werte die das Alphabet annimmt

    // eine zufällig große Primzahl für den Mod faktor
    val mod: long = math.pow(10, 9).toLong + 7 // sehr lange zahl die zufällig eine Primzahl ist lul
    // 

val patternHashes = HashSet[Int]()
val patterns = List("abc", "def", "ghi")  // t₁ bis tₖ
val m = patterns.head.length              // Länge der Muster

// 1. Hashes der Muster berechnen
for pattern <- patterns do
  patternHashes.add(hash(pattern))

// 2. Suche im Text s
for i <- 0 to s.length - m do
  val substring = s.substring(i, i + m)
  val subHash = hash(substring)

  if patternHashes.contains(subHash) then
    // Hash-Kollision absichern
    if patterns.contains(substring) then
      return i  // Treffer an Position i
