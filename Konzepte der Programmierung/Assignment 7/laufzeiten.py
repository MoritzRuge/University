def list_sum(xs):
	erg = 0
	for x in xs:
		erg = erg + x
	return erg

def sorted_zip(xs, ys):
	l = []
	mergesort(xs)
	mergesort(ys)
	for i in range(min(len(xs),len(ys))):
		l.append((xs[i],ys[i]))
	return l

def bauernmultiplikation(a,b):
	erg = 0
	while(a > 0):
		if(a % 2 == 1):
			erg = erg + b
		a = a//2
		b = b*2
	return erg