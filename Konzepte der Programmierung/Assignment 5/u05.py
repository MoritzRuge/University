"""
ToDo:
- Zeile soll aus 80 zeichen bestehen
    - mehr als 80 Zeichen wird das Wort abgeschnitten
- Funktion soll eine Liste von Zeilen wiedergeben
- Funktion soll die eingabe in Blocksatz formatieren
"""
def main():
    # ask for user input
    user_input = input("Bitte geben Sie ihren Text ein: ")

    #print the result
    print(Blocksatz(user_input.split()))


def Blocksatz(input_list):
    #duh code much
    #Variables and constants
    linelimit = 80
    lines = []
    current_line = []
    current_lenght = 0
    
    

    # checks if the user input is within linelinmit
    for word in input_list:
        
        # if the the word is longer then the limit it get cut off
        if len(word) > linelimit:
            word = word[:linelimit]

        # append the word to the current line
        current_line.append(word)
        current_lenght += len(word)

    # concatenate the the current line in line
    if current_line != []:
        lines.append(" ".join(current_line).ljust(linelimit))



    return lines



if __name__ == "__main__":
    main()

"""
Debug output:
#word to long
Bitte geben Sie ihren Text ein: thisisatestforaverylongwordwhichwillgetcutofffromthelinepossiblyandpossibleisnotawordwhichwillgetcutoffiguesssonowletssee
['thisisatestforaverylongwordwhichwillgetcutofffromthelinepossiblyandpossibleisnot']
"""