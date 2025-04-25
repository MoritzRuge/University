import random

def swap(a, i,j):
	temp = a[i]
	a[i] = a[j]
	a[j] = temp

def  quick_sort(a):

    def qsort(l,r):
        if r - l <= 1:
            return
        split = partition(a, l, r) # teilt liste in elemete kleiner pivot und größer pivot
        qsort(l, split)
        qsort(split + 1, r)

    qsort(0, len(a))

def partition(a, l, r):
    piv = a[l]
    split = l
    for i in range(l + 1, r):
        if a[i] < piv:
            split = split + 1
            swap(a, split, i)
    swap(a, l, split)
    return split


a = []
for i in range(20):
    a.append(random.randint(1, 100))

print(a)
print(quick_sort(a))