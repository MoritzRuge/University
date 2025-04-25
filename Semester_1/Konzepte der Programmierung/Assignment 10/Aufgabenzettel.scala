//Import
import scala.io.StdIn.readLine

// main Start of the Program, which subtask the user wants to choose
@main def start(): Unit =
  println("Choose the subtask: ")
  var input = readLine()

  input match
    case "1a" => subtask1a()
    case "1b" => subtask1b()
//
// Aufgabe 1 (a)
// t_chill = 13.12 + 0.6215 * t + (0.3965 * t - 11.37) * v^0.16
//
def subtask1a(): Unit =
  val numb_temp = readLine("Bitte geben Sie die Temperatur an: ").toInt
  val velocity = readLine("Bitte geben Sie die Windgeschwindigkeit an: ").toInt


  val t_chill = 13.12 + 0.6215 * numb_temp + (0.3965 * numb_temp - 11.37) * Math.pow(velocity, 0.16)

  println(s"Die gefühlte Temperatur beträgt $t_chill")


//
// Aufgabe 1 (b)
// endrekursive Funktion, die die eingegebene Zahl umdreht
// bsp: n=4256 -> n=6524
//

def subtask1b(): Unit =
  val numb_temp = readLine("Bitte geben Sie eine Nummer die, die Sie umdrehen wollen: ")

