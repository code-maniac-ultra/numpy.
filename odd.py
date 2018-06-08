def fillarray(size):
	num=[0]*size
	num=[random.randit(0,9) for i in range(size)]
	print (num)
	return num
def totalOdds(num,size):
	for i in range(size):
		if i % 2 ==0:
			odd = num[i]
			i+1
		print(odd)
