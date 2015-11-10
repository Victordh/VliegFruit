import global_variables

def insertion_sort(list):
    # append ('a') doesn't overwrite the already existing file
    f = open('out.txt', 'a')
    
    for i in range(1, len(list)):
        val = list[i]
        j = i - 1
        while (j >= 0) and (list[j] > val):
            f.write(str(list) + "\n")
            global_variables.counter += 1
            temp = list[j+1]
            list[j+1] = list[j]
            list[j] = temp
            j = j - 1
    # prints final (correct) list
    f.write(str(list) + "\n")
    f.write("Amount of steps needed: " + str(global_variables.counter))
    f.write("\n\n")
    return list
    
    # closes the output file
    f.close()

# swaps in list [list] the position of the [size] amount of numbers starting on position [pos]
def swap(size, pos, list):
    # append ('a') doesn't overwrite the already existing file
    f = open('out.txt', 'a')
    
    f.write(str(list) + "\n")
    global_variables.counter += 1
    y = []
    count = 0
    while count < size:
        y.append(list[count + pos])
        count += 1
    y.reverse()
    count = 0
    while count < size:
        list[count + pos] = y[count]
        count += 1
    f.write(str(list) + "\n")
    f.write("Amount of steps needed: " + str(global_variables.counter))
    f.write("\n\n")
    return list
    
    # closes the output file
    f.close()
