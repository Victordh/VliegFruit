# swaps in list [list] the position of the [size] amount of numbers starting on position [pos]
def swap(size, pos, listx):
    #global_variables.counter += 1
    y = []
    count = 0
    while count < size:
        y.append(listx[count + pos])
        count += 1
    y.reverse()
    print y
    count = 0
    
    while count < size:
        listx[count + pos] = y[count]
        count += 1
    return listx

# # lists that needs to be swapped
# lista = [2, 1, 3, 4, 5, 7, 6]
# listx = [7, 6, 5, 4, 3, 2, 1]
# listxx = [7, 6, 5, 4, 3, 2, 1]
# # goal list
# listy = [1, 2, 3, 4, 5, 6, 7]

# # if already in place, don't swap that position
# counterx = 0; # counter how many times loop through list
# counterxx = 0; # counter how many times set to 0 again
# while listx != listy:
#     counterx += 1  
#     #print counterx
#     if counterx > 7:
#         counterx = 0  
#         counterxx += 1
#         #print counterxx 
#     if listxx[counterx - 1] != listy[counterx - 1]:
#         print listxx[counterx - 1]
#         print listy[counterx - 1]
#         pos = (counterx - 1)
#         size = 2
#         print swap(size, pos, listx)    


    

     