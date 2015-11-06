from functions import *

x = 23, 1, 2, 11, 24, 22, 19, 6, 10, 7, 25, 20, 5, 8, 18, 12, 13, 14, 15 ,16, 17, 21, 3, 4, 9
x = list(x)
y = 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1
y = list(y)
z = list(y)

insertion_sort(x)
insertion_sort(y)

big_flip(z)