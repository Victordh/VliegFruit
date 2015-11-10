import global_variables

def insertion_sort(list):
    # append ('a') doesn't overwrite the already existing file
    f = open('out.txt', 'a')
    
    for i in range(1, len(list)):
        
        val = list[i]
        j = i - 1
        while (j >= 0) and (list[j] > val):
            
            # abort if more steps than previous attempt on same list
            if global_variables.counter > global_variables.best:
                f.write("Broken out after " + str(global_variables.counter) + " steps because it's more than " + str(global_variables.best))
                f.write("\n\n")
                return list
            
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
    
    # updates global variable best if best attempt on this list up until now
    if global_variables.counter < global_variables.best:
        global_variables.best = global_variables.counter
    
    return list
    
    # closes the output file
    f.close()

# swaps in list [list] the position of the [size] amount of numbers starting on position [pos]
def swap(size, pos, list):
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
    return list


def selection_sort(list):
    # append ('a') doesn't overwrite the already existing file
    f = open('out.txt', 'a')
    
    # appends the starting list
    f.write(str(list) + "\n")
    
    for i in range(1, len(list)):
        
        # abort if more steps than previous attempt on same list
        if global_variables.counter > global_variables.best:
            f.write("Broken out after " + str(global_variables.counter) + " steps because it's more than " + str(global_variables.best))
            f.write("\n\n")
            return list
        
        # if number isn't on the right spot yet, swaps once so it is and appends the new list
        if i != list[i - 1]:
            swap(list.index(i) + 1 - (i - 1), i - 1, list)
            f.write(str(list) + "\n")
    
    f.write("Amount of steps needed: " + str(global_variables.counter))
    f.write("\n\n")
    
    # updates global variable best if best attempt on this list up until now
    if global_variables.counter < global_variables.best:
        global_variables.best = global_variables.counter
    
    # closes the output file
    f.close()

#def short_list(list):
    # if numbers are already on the correct spot (only at start or end), make the list shorter and use the shorter one instead
