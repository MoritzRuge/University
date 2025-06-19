import java.security.MessageDigest

// Hilfsfunktion um eine Hash fuer SHA-256 zu erzeugen Return String(Bytes), aus Aufgabe 1a
def sha256(input: String): String =
  val sha256 = MessageDigest.getInstance("SHA-256")
  val hashWert = sha256.digest(input.getBytes("UTF-8"))
  hashWert.map("%02x".format(_)).mkString

// Erzeugen der Datenstruktur fuer eine einfach verkettete Liste mit Hashreferenz
// data: inhalt des Knotens
// prevHash Der SHA-256 des vorhergehenden Knotens
// nextHash Verweisst auf den naechsten Knoten in der Liste
case class Node(data: String, prevHash: String, nextHash: Option[Node])

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
        val newNode = Node(data, prevHash, Option(previousNode))
        prevHash = sha256(prevHash + data)
        previousNode = newNode
        startNode = newNode

    startNode

@main def main(): Unit =
    val liste = buildingList(List("Alice", "Bob", "Charlie"))

    def printList(node: Node): Unit =
        println(s"Daten: ${node.data}")
        println(s"PrevHash: ${node.prevHash}")
        println()
        node.nextHash.foreach(printList)

    printList(liste)
