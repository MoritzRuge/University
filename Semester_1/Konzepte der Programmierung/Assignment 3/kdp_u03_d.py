# Zahlen einlesen, bis der user eine 0 eingibt, danach soll der Druchschnitt der eingegebenen Zahlen ausgegeben werden.
counter = 0 
total = 0
while True:
    x = int(input("Bitte Zahl eingeben: "))
    if x == 0:
        break
    total += x
    counter += 1

result = total / counter
print(int(result))

