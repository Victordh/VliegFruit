def insertion_sort(s):
    # append ('a') doesn't overwrite the already existing file
    f = open('out.txt', 'a')
    
    count = 0
    for i in range(1, len(s)):
        val = s[i]
        j = i - 1
        while (j >= 0) and (s[j] > val):
            f.write(str(s) + "\n")
            count += 1
            temp = s[j+1]
            s[j+1] = s[j]
            s[j] = temp
            j = j - 1
    # prints final (correct) list
    f.write(str(s) + "\n")
    f.write("Amount of steps needed: " + str(count))
    f.write("\n\n")
    return s
    
    # closes the output file
    f.close()

def big_flip(s):
    # append ('a') doesn't overwrite the already existing file
    f = open('out.txt', 'a')
    
    # TODO make count global and don't reset it when combining different sorts
    count = 1
    length = len(s)
    # prints first (incorrect) list
    f.write(str(s) + "\n")
    for i in range(0, length / 2):
        temp = s[length - i - 1]
        s[length - i - 1] = s[i]
        s[i] = temp
    # prints final (correct) list
    f.write(str(s) + "\n")
    f.write("Amount of steps needed: " + str(count))
    f.write("\n\n")
    return s
    
    # closes the output file
    f.close()

# swaps in list [i] the position of the [size] amount of numbers starting on position [pos]
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