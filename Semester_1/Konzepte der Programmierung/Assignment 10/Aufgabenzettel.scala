//Import
import scala.io.StdIn.readLine
import scala.collection.mutable.ArrayBuffer

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
  val input = readLine("Bitte geben Sie eine Nummer die, die Sie umdrehen wollen: ")
  var result = swap(input)
  println(s"Die Umgedrehte Eingabe: $result")

def swap(input: String): String =
  if input.isEmpty then 
    "" // Rekursionsanker
  else
    swap(input.tail) + input.head


//
// Aufgabe 2
// type Uhrzeit = (Int, Int, Int)
// val z : Uhrzeit = (14,15,0) //Startzeit der Vorlesung
//
// - istUhrzeit - überprüft, ob ein gegebenes Tripel aus ganzen Zahlen tatsächlich eine gültige Uhrzeit ist.
// - tick erhält eine Uhrzeit und liefert die Uhrzeit eine Sekunde später. (Beispiel: tick(22,59,59) liefert (23,0,0))
// - kcit ist die Umkehrfunktion von tick.
// - Die Funktion addSekunde, addMinuten sowie addStunden erhalten eine gültige Uhrzeit und eine ganze Zahl und addieren diese ganze Zahl auf die Sekunden, Minuten bzw. Sekunden.
//

def task2(): Unit =
  type Uhrzeit(int, int, int)
  val z : Uhrzeit = (14, 15, 0)
  println(z)
