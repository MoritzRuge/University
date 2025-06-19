import scala.util.hashing.Hashing


@main def run(): Unit =

  val h = summon[Hashing[String]]
  val hashWert = h.hash("Hallo")

  println(hashWert)

