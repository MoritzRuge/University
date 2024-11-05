#Summe aus 1 bis n berechnene mit for loop
n = int(input("Bitte die Range angeben: "))

def Summe(n):
    sum = 0
    for i in range(1,n+1):
        sum = sum + int(i) 
    print(sum)


def Summebesser(n):
    print(int(n * (n+1) /2))

Summe(n)
Summebesser(n)
