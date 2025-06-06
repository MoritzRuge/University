import scala.io.StdIn.readLine


def fibo(zahl: Int): Int =
  if zahl <= 1 then
    return zahl
  else
    return fibo(zahl - 1) + fibo(zahl - 2)


@main def start(): Unit = 
  println("Bitte zahl eingeben: ")
  var input = readLine().toInt

  for i <- 0 to input.toInt do 
    print(s"f($i): " + fibo(i) + "\n")


