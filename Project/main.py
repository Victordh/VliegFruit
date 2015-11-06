from functions import *
import random

# overwrites out.txt and closes right away for an empty file
f = open('out.txt', 'w')
f.close()

x = random.sample(xrange(1, 26), 25)
y = random.sample(xrange(1, 26), 25)
z = random.sample(xrange(1, 26), 25)

# x = 23, 1, 2, 11, 24, 22, 19, 6, 10, 7, 25, 20, 5, 8, 18, 12, 13, 14, 15 ,16, 17, 21, 3, 4, 9
# x = list(x)
# y = 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1
# y = list(y)
# z = list(y)

insertion_sort(x)
insertion_sort(y)

big_flip(z)
insertion_sort(z)