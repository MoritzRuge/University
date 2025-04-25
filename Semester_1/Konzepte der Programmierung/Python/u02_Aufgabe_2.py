def main():
    while True:
        print("1.Flächenberechnung\n2.Schaltjahr\n3.Mersennezahl\n4.Umwandler\n5.Cinematicket\nExit\nBitte wählen Sie mittels 1-5 oder geben Sie Exit ein um das Programm zu beenden.")
        value = input().title()
        match value:
            case "1":
                Flaechenberechnung()
                Exitfunc()
            case "2":
                Schaltjahr()
                Exitfunc()
            case "3":
                MersenneZahl()
                Exitfunc()
            case "4":
                Umwandler()
                Exitfunc()
            case "5":
                Cinematicket()
                Exitfunc()
            case "Exit":
                quit()
            case _:
                print("Entschuldigung, diese Anweisung verstehe ich nicht.")

#Funktion für die Berechne der Fläche eines Dreiecks mit Grundseitenlnge a und höhe h
def Flaechenberechnung():
    print("Hallo, willkommen bei der Dreiecks Flächenberechnung. Bitte gebe die Grundseitenlänge a und die höhe h ein.")
    a = int(input("a: ")) # user input für die Variable a
    h = int(input("h: ")) # user input für die Variable h
    area = 0.5 * a * h # Formel für die Flächenberechnung A = 0,5 * a * h
    print(f"Die Fläche beträgt {area:.2f}") # Print das Endergebnis

# User gibt uns eine Zahl/Jahr Funktion gibt genau dann True zurück, wenn die Zahl/Jahr ein Schaltjahr
# im Gregorianischen Kalender ist.
# Jahreszahl muss durch 4 teilbar sein
# Die Jahreszahl darf nicht restlos durch 100 teilbar sein
#Ist eine Jahreszahl, die restlos durch 100 teilbar ist, ebenfalls restlos durch 400 teilbar, ist das Jahr dennoch ein Schaltjahr.
def Schaltjahr():
    print("Willkommen im Schaltjahrrechner, bitte geben Sie die Gewünschte Jahreszahl ein.")
    year = int(input("Year: ")) # user Input für das Jahr
    modulus_four = year % 4 # Erstellt den Modulus für den Input durch 4
    modulus_hundred = year % 100 # Erstellt den Modulus für den Input von 100
    modulus_four_hundred = year % 400 # Berechnet den Modulus für 400
    if modulus_four == 0: # Wenn die Zahl Restlos durch 4 teilbar ist gehen wir in die nächste if Schleife
        if modulus_hundred == 0 and modulus_four_hundred == 0: # Restlos durch 100 und 400 teilbar return true
            print(True)
        elif modulus_hundred == 0: # wenn nur durch restlos durch 100 teilbar retun false
            print(False)
        else: # wenn nur restlos durch 4 teilbar dann true
            print(True)
    else: # Zahl nicht restlos durch 4 teilbar retun false
        print(False)

def MersenneZahl():
    # Mersenne Zahl: 2^n - 1 in Bit Operationen
    # Bit shift nach links entspricht 2^n
    n = int(input("n: ")) # get user input and convert str to int
    n = n << n # perfom a bitshift to the left, which corrospons to n * 2^n
    print(f"Die Mersennezahl ist: {n-1}") # #f-string format to insert a variable into the string and perform a arthimetic operation e.g. n-1


# User inputs a letter and gets converted to a chr()
def Umwandler():
    print("Hallo, Willkommen beim Umwandler. Bitte geben Sie ihren Buchstaben ein.")
    while True:
        user_input = input("Input: ")
        if user_input.isupper() == True: # Check if the user input is a Upper character
            ascii_number = ord(user_input.lower()) # If upper True get the ascii number for the lower case letter
            reverse_letter = chr(ascii_number) # reverse back to a letter
            print(f"Output: {reverse_letter}") # output the reversed letter
            break # breaks the loop
        elif user_input.islower() == True: # Check if the user inputs a lower case character
            ascii_number = ord(user_input.upper()) # reverses the input to get the uppercase dezimal characters
            reverse_letter = chr(ascii_number) # revert the dez back to an upper case character
            print(f"Output: {reverse_letter}") # print out the reversed character in f string format
            break # breaks the loop
        else: # inputs other than letters will not be accepted
            print("Zahlen/Sonderzeichen sind nicht erlaubt.")

def Cinematicket():
    # Kinder unter 12J. zahlen 10€ jugendliche bis 18J 12€ Erwachsene 14€ Rentner ab 65J 12€
    print("Willkommen im Kino, wie alt sind Sie?")
    while True:
        age = int(input("Alter: "))
        if age < 12: # check if age is less then 12
            print("Sie zahlen 10€")
            break # breaks while loop
        elif age < 18: # check if age is less then 18
            print("Sie zahlen 12€")
            break # breaks while loop
        elif age < 65: # check if age is less then 65
            print("Sie zahlen 14€")
            break # breaks while loop
        else: # age above 65
            print("Sie zahlen 12€")
            break # breaks while loop




# Exit function for quality of life
def Exitfunc():
    while True: # endless loop
        x = input("möchten Sie zum Menü zuückkehren?(Y/n): ").title() # gets user input, changes the first input letter to an upper case letter
        if x == "Y" or x == "": # checks if the user inputs Y or nothing (defaults to Y)
            break # breaks the while loop
        elif x == "N": # if user input is N, quits the program
            quit()
        else:
            print("Nicht bekannte Eingabe, versuchen Sie es mit Y oder n.") # catches faulty user input






# Vorsichtsmaßnahme erklärung muss ich noch raussuchen...duh
if __name__ == "__main__":
    main()
