// Todo: Implimentiere die Suchalgorithmen mit festverbauter liste oder liste zum eingeben
//

// Import


// Selection Sort
// Suche das kleinste Element und setzte es an die erste Stelle usw.
// Benötigt eine swap funktion zum tauschen der Elemente und die Normale Sortingfunktion
//

// Main funktion
import scala.compiletime.ops.double

@main def Start(): Unit =
  val Test = Array(10,20,1,5,4,36,78,100,50,49)
  SelectionSort(Test)
  var result = InsertionSort(Test)
  println("SelectionSort: " + Test.mkString(", "))
  println("InsertionSort: " + result.mkString(", "))

def SelectionSort(Liste: Array[Int]): Unit =
  //variablen
  val n: Int = Liste.length
  
  // loop trough the entire list and set i to the minimum e.g. the first elemetn is minimum
  // in the second loop we check if i is still the minimum
  for i <- 0 to n-1 do
    var min_index = i
    
    // check if the element after i (i+1) is smaller then i, if so set min_index = j
    for j <- i+1 to n-1 do
      if Liste(j) < Liste(min_index) then
        min_index = j //update the candidate
    //after we made the check if i or j is smaller, we swap the element
    swap(Liste, i, min_index)

def swap(Liste: Array[Int], i: Int, j: Int): Unit =
  var temp = Liste(i)
  Liste(i) = Liste(j)
  Liste(j) = temp

// InsertionSort Programm
def InsertionSort(Liste: Array[Int]): Array[Int] =
    val arr = Liste.clone()
    val n: Int = Liste.length

    for i <- 1 to n - 1 do
        var key = arr(i)
        var j = i - 1

        while j >= 0 && arr(j) > key do
            arr(j+1) = arr(j)
            j -= 1
        arr(j+1) = key
    return arr


// Merge Sort Programm
