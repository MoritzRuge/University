//**Tag 1:** Schreibe ein Programm, das prüft, ob eine Zahl gerade oder ungerade ist.

// Imports
import scala.io.StdIn.readLine

@main def main(): Unit =
    val input = readLine("Bitte Zahl eingeben: ")
    val number = input.toInt
    var result = isEven(number)

    if result then
        println("Is Even")
    else
        println("Is not Even")

def isEven(number: Int): Boolean =
    number % 2 == 0
