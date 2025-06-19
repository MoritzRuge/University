import java.security.MessageDigest


@main def run(): Unit =

  val message = "Hello World"
  val sha256 = MessageDigest.getInstance("SHA-256")
  val hashWert = sha256.digest(message.getBytes("UTF-8"))

  // Bytes nach Hex-String umwandeln
  val hashHex = hashWert.map("%02x".format(_)).mkString

  println(hashHex)

