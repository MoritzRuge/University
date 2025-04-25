import random

def merge_sort(a):
    n = len(a)
    if n <= 1:
        return a
    left = a[:n//2] # von 0 bis n//2
    right = a[n//2:] # von n//2 bis ende der Liste
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left,right)

def merge(left, right):
    a = [] # ergebnisliste a
    l_index = 0
    r_index = 0
    while l_index < len(left) and r_index < len(right):
        if left[l_index] < right[r_index]:
            a.append(left[l_index])
            l_index = l_index + 1

        else:
            a.append(right[r_index])
            r_index = r_index + 1

    while l_index < len(left):
        a.append(left[l_index])
        l_index = l_index + 1
    while r_index < len(right):
        a.append(right[r_index])
        r_index = r_index + 1

    return a

a = []
for i in range(20):
    a.append(random.randint(1, 100))

print(a)
print(merge_sort(a))
    