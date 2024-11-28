""" Merge Sort nur itereativ 

ToDo:
- Teile die Liste in Abschnitte bestimmer Größe 2,4,6,8...,n
- Mische zwei aufeinanderfolgende Abschnitte in einer sortierten Reihenfolge zusammen
- Wiederhole diese mit verdoppelter Abschnittsgröße, bis die Liste vollständig sortiert ist
"""
# Bottem up Merge funktion
# Merge_sort funktion
# Teile die Liste in Abschnitte ein
def Merge_Sort(liste):
    anker = 1 # Definiert die aktuelle Länge der Teilstücke, die gemischt werden
    n = len(liste) # länge der Liste
    
    # Schleife für das Durchmischen, bis die gesamte Liste sortiert ist
    while anker < n:
        # itteration durch die Liste in Schritten von 2 * anker
        for firstitem in range(0, n, 2*anker):
            miditem = min(firstitem + anker, n) # ermittelt den min wert für den ersten wert
            enditem = min(firstitem + 2 * anker, n) # ermittelt im abstand von 2 * anker (2,4,6,8) den endwert der teilliste

            # Mischen der beiden teilstücke
            # wir geben die ermittelten Werte weiter
            merged = merge(liste[firstitem:miditem], liste[miditem:enditem])
            # wir überschreiben das erste item:bis zu länge von der funktion merged
            liste[firstitem:firstitem + len(merged)] = merged 
    
        # verdoppelt die Teillänge
        anker *= 2
    return liste

def merge(left, right):
    i = j = 0
    liste = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            liste.append(left[i])
            i += 1
        else:
            liste.append(right[j])
            j += 1

    liste.extend(left[i:])
    liste.extend(right[j:])
    return liste

# Testliste
a = [ 3,4,8,5,1,5]
sorted_a = Merge_Sort(a)
print(sorted_a)
