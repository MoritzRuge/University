def swap(a, i,j):
	temp = a[i]
	a[i] = a[j]
	a[j] = temp

def selection_sort(a):
	for i in range(len(a)):
		min_index = i
		j = i + 1
		while j < len(a):
			if a[j] < a[min_index]:
				min_index = j
			j = j + 1
		swap(a, i, min_index)
		

a = [1,7,9,4,5,2,10,20,44]

selection_sort(a)
print(a)