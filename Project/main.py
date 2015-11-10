import global_variables
from functions import *
import random

global_variables.initialise()

# overwrites out.txt and closes right away for an empty file
f = open('out.txt', 'w')
f.close()

# 25 random lists
for i in range(25):
    n_random_list = random.sample(xrange(1, 26), 25)
    global_variables.counter = 0
    selection_sort(n_random_list)