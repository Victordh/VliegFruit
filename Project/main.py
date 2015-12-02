import global_variables
from functions import *
from sorts import *
import random

global_variables.initialise()

# overwrites out.txt and closes right away for an empty file
f = open('out.txt', 'w')
f.close()

# 25 random lists
for i in range(25):
        
    # create a random list of length 25 (and a duplicate of it)
    n_random_list = random.sample(xrange(1, 26), 25)
    n_random_list = [n_random_list[i : i+1] for i in range(len(n_random_list))]
    duplicate = list(n_random_list)
    
    # get a result with selection_sort
    global_variables.counter = 0
    selection_sort(n_random_list)
    
    # try to get a better result with insertion_sort (doesn't seem to be possible)
    global_variables.counter = 0
    insertion_sort(duplicate)
    
    # reset the global variable best
    global_variables.best = 301

genoom_van_de_site = 23, 1, 2, 11, 24, 22, 19, 6, 10, 7, 25, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9
genoom_van_de_site = list(genoom_van_de_site)
duplicate = list(genoom_van_de_site)

# get a result with selection_sort (18) (other group has 16)
global_variables.counter = 0
selection_sort(genoom_van_de_site)

# try to get a better result with insertion_sort (doesn't work)
global_variables.counter = 0
insertion_sort(duplicate)

# reset the global variable best
global_variables.best = 301
