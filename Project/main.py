import global_variables
from functions import *
import random

global_variables.initialise()

# overwrites out.txt and closes right away for an empty file
f = open('out.txt', 'w')
f.close()

# 25 random lists
for i in range(25):
        
    # create a random list of length 25 (and a duplicate of it)
    n_random_list = random.sample(xrange(1, 26), 25)
    duplicate = list(n_random_list)
    
    # get a result with selection_sort
    global_variables.counter = 0
    selection_sort(n_random_list)
    
    # try to get a better result with insertion_sort (doesn't seem to be possible)
    global_variables.counter = 0
    insertion_sort(duplicate)
    
    # reset the global variable best
    global_variables.best = 999
