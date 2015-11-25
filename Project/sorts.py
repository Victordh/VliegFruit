import global_variables
from functions import *
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
