import java.security.MessageDigest

// Hilfsfunktion um eine Hash fuer SHA-256 zu erzeugen Return String(Bytes), aus Aufgabe 1a
def sha256(input: String): String =
  val sha256 = MessageDigest.getInstance("SHA-256")
  val hashWert = sha256.digest(input.getBytes("UTF-8"))
  hashWert.map("%02x".format(_)).mkString

// Hilfsfunktion um einen Hash fue SHA-256 zu erzeigen - return Array[Bytes]
def sha256Bytes(input: String): Array[Byte] =
    val sha256 = MessageDigest.getInstance("SHA-256")
    sha256.digest(input.getBytes("UTF-8"))

// Erzeugen der Datenstruktur fuer eine einfach verkettete Liste mit Hashreferenz
// data: inhalt des Knotens
// prevHash Der SHA-256 des vorhergehenden Knotens
// nextHash Verweisst auf den naechsten Knoten in der Liste
case class Node(
    data: String,
    prevHash: String,
    hash: String,
    nextHash: Option[Node],
    Nonce: Int
)

def buildingList(strings: List[String]): Node =
    val initialHash = "0" * 64 // setzte den ersten Hashwert auf 64 Nullen als Startwert
    var prevHash = initialHash
    var startNode: Node = null
    var previousNode: Node = null

    // wir drehen die Liste um da wir noch keine Werte fuer den zweiten Knoten haetten
    // d.h. wir fangen hinten an und rechnen die Liste umgedreht durch
    val reversed = strings.reverse

    for i <- 0 until reversed.length do
        val data = reversed(i)
        val (nonce, hash) = findValidNonce(data, prevHash)
        val newNode = Node(data, prevHash, hash, Option(previousNode), nonce)
        prevHash = hash
        previousNode = newNode
        startNode = newNode

    startNode // return die startNode

// Checken ob die letzten Acht zeichen Nullen sind
def hashEndsWithEightZeroBits(hash: Array[Byte]): Boolean =
    hash.last == 0 // oder 0.toByte was aber das gleiche ist... 0

// Suche nach gueltiger Nonce
def findValidNonce(data: String, prevHash: String): (Int, String) =
    var nonce = 0
    var hashWert: Array[Byte] = Array(1.toByte) // Startwert nicht 0, damit Schleife startet
    var hashHex = ""

    // while do loop - solange bis wir am Ende 8 Nullen haben; 8 Nullen = 00 in Byte
    while !hashEndsWithEightZeroBits(hashWert) do
        val input = s"$data|$nonce|$prevHash" // wir trennen die inputs um moegliche zufaellige Kollision zu vermeiden
        hashWert = sha256Bytes(input)
        nonce += 1

    hashHex = hashWert.map("%02x".format(_)).mkString// Formatiere Array[Bytes] in String um
    (nonce - 1, hashHex) // Korrektur, da nach Schleife +1 ist


@main def main(): Unit =
    val liste = buildingList(List("Alice", "Bob", "Charlie"))

    def printList(node: Node): Unit =
        println(s"Daten: ${node.data}")
        println(s"PrevHash: ${node.prevHash}")
        println(s"Nonce:    ${node.Nonce}")
        println(s"Hash:     ${node.hash}")
        println()
        node.nextHash.foreach(printList)

    printList(liste)
