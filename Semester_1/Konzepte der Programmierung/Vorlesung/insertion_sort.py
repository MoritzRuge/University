def insertion_sort(a):
	for i in range(len(a)):
		j = i
		while j > 0 and a[j] < a[j-1]:
			swap(a,j,j-1)
			j = j - 1
			
def swap(a, i,j):
	temp = a[i]
	a[i] = a[j]
	a[j] = temp

a = [ 1,6,3,7,9,2]

insertion_sort(a)
print(a)