import global_variables
from functions import *
import random

global_variables.initialise()

# overwrites out.txt and closes right away for an empty file
f = open('out.txt', 'w')
f.close()

x = random.sample(xrange(1, 26), 25)
y = random.sample(xrange(1, 26), 25)
z = random.sample(xrange(1, 26), 25)

global_variables.counter = 0
insertion_sort(x)

global_variables.counter = 0
insertion_sort(y)

global_variables.counter = 0
swap(25, 0, z)
insertion_sort(z)
