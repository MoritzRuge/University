# erstelle list a mit beliebigen zahlen
# eine zahl x heißt Mehrheitselement von a, wenn x an mindestens [n/2] + 1 Positionen von a vorkommt

a = [1,1,1,1,2]

leng = round(len(a) / 2)
n = len(a)

a1 = a[:leng]
a2 = a[leng:]
def mehrheitselement(n):
    for i in range(n):
        count = 0

        for j in range(n):
            if a[i] == a[j]:
                count += 1

        if count > n // 2:
            return(a[i])
        
mehrheitselement(a)