# "Locks" begin en einde als ze al op de juiste plek staan. 

# expected output: [5, 6, 4, 8, 7]
# listx = [1, 2, 3, 5, 6, 4, 8, 7, 9, 10]
listx = [1, 3, 2, 5, 6, 4, 9, 7, 8, 10] # [3, 2, 5, 6, 4, 9, 7, 8]
list_goal = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
LEN = len(listx)

while listx[0] == list_goal[0]:
        listx = listx[1:LEN]
        list_goal = list_goal[1:LEN]
        print listx
        # print list_goal

while listx[(len(listx) - 1)] == list_goal[(len(list_goal) - 1)]:
    listx = listx[0:(len(listx) - 1)] 
    list_goal = list_goal[0:(len(list_goal) - 1)]   
    print listx          