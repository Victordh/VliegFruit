import global_variables
import random

def insertion_sort(genome):
    # append ('a') doesn't overwrite the already existing file
    f = open('out.txt', 'a')
    
    for i in range(1, len(genome)):
        
        val = genome[i]
        j = i - 1
        while (j >= 0) and (genome[j] > val):
            
            # abort if more steps than previous attempt on same genome
            if global_variables.counter > global_variables.best:
                f.write("Broken out after " + str(global_variables.counter) + " steps because it's more than " + str(global_variables.best))
                f.write("\n\n")
                return genome
            
            f.write(str(genome) + "\n")
            global_variables.counter += 1
            temp = genome[j+1]
            genome[j+1] = genome[j]
            genome[j] = temp
            j = j - 1
    
    # prints final (correct) genome
    f.write(str(genome) + "\n")
    f.write("Amount of steps needed: " + str(global_variables.counter))
    f.write("\n\n")
    
    # updates global variable best if best attempt on this genome up until now
    if global_variables.counter < global_variables.best:
        global_variables.best = global_variables.counter
    
    return genome
    
    # closes the output file
    f.close()

# swaps in genome [genome] the position of the [size] amount of numbers starting on position [pos]
def swap(size, pos, genome):
    global_variables.counter += 1
    y = []
    count = 0
    
    while count < size:
        y.append(genome[count + pos])
        count += 1
    y.reverse()
    count = 0
    
    while count < size:
        genome[count + pos] = y[count]
        count += 1
    return genome

# takes a genome and returns it with part of random size at random position inverted
def random_inversion(genome):
    random_size = random.randint(2,25)
    random_pos = random.randint(0, 25 - random_size)
    return swap(random_size, random_pos, genome)

def selection_sort(genome):
    # append ('a') doesn't overwrite the already existing file
    f = open('out.txt', 'a')
    
    # appends the starting genome
    f.write(str(genome) + "\n")
    
    for i in range(1, len(genome)):
        
        # abort if more steps than previous attempt on same genome
        if global_variables.counter > global_variables.best:
            f.write("Broken out after " + str(global_variables.counter) + " steps because it's more than " + str(global_variables.best))
            f.write("\n\n")
            return genome
        
        # if number isn't on the right spot yet, swaps once so it is and appends the new genome
        if i != genome[i - 1]:
            swap(genome.index(i) + 1 - (i - 1), i - 1, genome)
            f.write(str(genome) + "\n")
    
    f.write("Amount of steps needed: " + str(global_variables.counter))
    f.write("\n\n")
    
    # updates global variable best if best attempt on this genome up until now
    if global_variables.counter < global_variables.best:
        global_variables.best = global_variables.counter
    
    # closes the output file
    f.close()

#def shorten_genome(genome):
    # if numbers are already on the correct spot (only at start or end), make the genome shorter and use the shorter one instead
