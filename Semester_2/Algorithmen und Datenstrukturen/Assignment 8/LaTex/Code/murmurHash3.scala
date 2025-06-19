import scala.util.hashing.MurmurHash3


@main def run(): Unit =

  val text = "Hallo Welt"
  val hashWert = MurmurHash3.stringHash(text)

  println(hashWert)

