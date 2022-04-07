n2 = 1
n1 = 2
n = 0
esum = 2

while n < 4000000:
	n = n2 + n1
	n2 = n1
	n1 = n
	if n % 2 == 0:
		esum += n
		print(esum)