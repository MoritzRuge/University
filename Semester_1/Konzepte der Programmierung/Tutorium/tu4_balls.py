"""
Untersuchen Sie experimentell, was passiert, wenn man n B¨alle zuf¨allig gleichverteilt
in n Eimer wirft. Wie viele Eimer bleiben leer? Wie viele Eimer erhalten genau
einen Ball, wie viele Eimer erhalten genau zwei B¨alle, usw? Machen Sie fur ¨ n = 10,
100, und 1000 jeweils 100 Experimente, und bestimmen Sie fur jedes ¨ n auch die
maximale Anzahl an B¨allen, die in einem Eimer landen. (Der Erwartungswert fur ¨
das Maximum ist ungef¨ahr ln n/ ln ln n.)
"""
import random

def balls():
    n = int(input("wieviele Bälle wollen Sie werfen? "))
    Buckets = {}
    # create dictionaries from 0 to n
    for i in range(1, n+1):
        Buckets[i] = 0
    for j in range (1, n+1):
        rannumber = random.randint(1, n+1)
        Buckets[rannumber] = Buckets[j] + 1
    #for _ in range (1, n+1):


    print(Buckets)
        

balls()