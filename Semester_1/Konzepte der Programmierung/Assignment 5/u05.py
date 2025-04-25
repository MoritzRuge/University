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
    result = Blocksatz(user_input.split())

    for line in result:
        print(f"|{line}|")

def Blocksatz(input_list):
    #duh code much
    #Variables and constants
    linelimit = 80
    lines = []
    current_line = []
    current_length = 0
    
    

    # checks if the user input is within linelinmit
    for word in input_list:
        
        # if the the word is longer then the limit it get cut off
        if len(word) > linelimit:
            word = word[:linelimit]

        # check if the word is able to fit on the line
        if current_length and len(word) and len(current_line) > linelimit:
            # if the word is to long to fit, format the current line into blocksatz and create a new line
            lines.append(format_block(current_line, linelimit))
            current_length = 0
            current_line = []

        # append the word to the current line
        current_line.append(word)
        current_length += len(word)

    # concatenate the the current line in line
    if current_line != []:
        lines.append(" ".join(current_line).ljust(linelimit))



    return lines

def format_block(words, linelimit):
    """Formating one line in Blocksatz"""
    if len(words) == 1:
        return words[0].ljust(linelimit)
    
    #calculatin the total length in the given list
    total_length = sum(len(word) for word in words)
    spaces_needed = linelimit - total_length
    spaces_between_words, extra_spaces = divmod(spaces_needed, len(words)-1)

    justified_line = ""
    for i, word in enumerate(words[:-1]):
        justified_line += word
        justified_line += " " * (spaces_between_words + (1 if i < extra_spaces else 0))
    justified_line += words[-1]

    return justified_line



if __name__ == "__main__":
    main()

"""
Debug output:
#word to long
Bitte geben Sie ihren Text ein: thisisatestforaverylongwordwhichwillgetcutofffromthelinepossiblyandpossibleisnotawordwhichwillgetcutoffiguesssonowletssee
['thisisatestforaverylongwordwhichwillgetcutofffromthelinepossiblyandpossibleisnot']
"""