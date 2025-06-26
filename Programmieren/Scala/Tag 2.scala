//* **Tag 2:** FizzBuzz (Zahlen 1–100, ersetze durch „Fizz“ für 3, „Buzz“ für 5, „FizzBuzz“ für beides)

@main def day2(): Unit = 

    //for i <- 1 to 100 do
    //    if i % 3 == 0 && i % 5 == 0 then
    //        println("FizzBuzz")
    //    else if i % 5 == 0 then
    //        println("Buzz")
    //    else if i % 3 == 0 then
    //        println("Fizz")
    //    else
    //        println(i)

    bonusaufgabe()


// Bonusaufgabe versuchen, FizzBuzz funktional mit map zu schreiben
def bonusaufgabe(): Unit =
    val zahlen = (1 to 100).toList
    val fizzbuzzListe = zahlen.map(x =>
        if x % 3 == 0 && x % 5 == 0 then "FizzBuzz"
        else if x % 3 == 0 then "Fizz"
        else if x % 5 == 0 then "Buzz"
        else x.toString)
    println(fizzbuzzListe)
        