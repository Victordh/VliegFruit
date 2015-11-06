import global_variables

def insertion_sort(s):
    # append ('a') doesn't overwrite the already existing file
    f = open('out.txt', 'a')
    
    for i in range(1, len(s)):
        val = s[i]
        j = i - 1
        while (j >= 0) and (s[j] > val):
            f.write(str(s) + "\n")
            global_variables.counter += 1
            temp = s[j+1]
            s[j+1] = s[j]
            s[j] = temp
            j = j - 1
    # prints final (correct) list
    f.write(str(s) + "\n")
    f.write("Amount of steps needed: " + str(global_variables.counter))
    f.write("\n\n")
    return s
    
    # closes the output file
    f.close()

# swaps in list [s] the position of the [size] amount of numbers starting on position [pos]
def swap(size, pos, s):
    # append ('a') doesn't overwrite the already existing file
    f = open('out.txt', 'a')
    
    f.write(str(s) + "\n")
    global_variables.counter += 1
    y = []
    count = 0
    while count < size:
        y.append(s[count + pos])
        count += 1
    #print y
    y.reverse()
    #print y
    count = 0
    while count < size:
        s[count + pos] = y[count]
        count += 1
    f.write(str(s) + "\n")
    f.write("Amount of steps needed: " + str(global_variables.counter))
    f.write("\n\n")
    return s
    
    # closes the output file
    f.close()
