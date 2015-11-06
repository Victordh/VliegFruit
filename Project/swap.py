#Swaps in list [i] the position of the [size] amount of numbers starting on position [pos]
def swap(size, pos, i):
	
	y = []
	count = 0
	while count < size:
		y.append(i[count + pos])
		count += 1
	#print y
	y.reverse()
	print y
	count = 0
	while count < size:
		i[count + pos] = y[count]
		count += 1
	return i