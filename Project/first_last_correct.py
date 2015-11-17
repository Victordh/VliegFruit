
# Hard coded. NIE ZO MOOI MAN. Compares the first and the last of listx with list_goal. If already right
# position (for example: listx[0] == list_goal[0]), "remove from list". 


# EXAMPLE WITH LIST WITH THE FIRST 2 AND THE LAST 2 IN THE RIGHT PLACE
listx = [1, 2, 4, 3, 5, 6, 7, 8, 9, 10]
list_goal = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
LEN = len(listx)
print listx
if listx[0] == list_goal[0]:
    listx = listx[1:LEN]
    list_goal = list_goal[1:LEN]
    # print listx
    # print list_goal
if listx[(len(listx) - 1)] == list_goal[(len(list_goal) - 1)]:
    listx = listx[0:(len(listx) - 1)] 
    list_goal = list_goal[0:(len(list_goal) - 1)]   
    # print listx  
    # print list_goal 
LEN = len(listx)
if listx[0] == list_goal[0]:
    listx = listx[1:LEN]
    list_goal = list_goal[1:LEN]
    # print listx
    # print list_goal
if listx[(len(listx) - 1)] == list_goal[(len(list_goal) - 1)]:
    listx = listx[0:(len(listx) - 1)] 
    list_goal = list_goal[0:(len(list_goal) - 1)]   
    # print listx  
print listx #list after removing the first 2 and the last 2 from list if already right position

# EXAMPLE WITH LIST WITH THE FIRST 2 IN THE RIGHT PLACE
listy = [1, 2, 4, 3, 5, 6, 7, 8, 10, 9]
list_goal = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
LEN = len(listy)
print listy
if listy[0] == list_goal[0]:
    listy = listy[1:LEN]
    list_goal = list_goal[1:LEN]
    # print listy
    # print list_goal
if listy[(len(listy) - 1)] == list_goal[(len(list_goal) - 1)]:
    listy = listy[0:(len(listy) - 1)] 
    list_goal = list_goal[0:(len(list_goal) - 1)]   
    # print listy  
    # print list_goal 
LEN = len(listy)
if listy[0] == list_goal[0]:
    listy = listy[1:LEN]
    list_goal = list_goal[1:LEN]
    # print listy
    # print list_goal
if listy[(len(listy) - 1)] == list_goal[(len(list_goal) - 1)]:
    listy = listy[0:(len(listy) - 1)] 
    list_goal = list_goal[0:(len(list_goal) - 1)]   
    # print listy  
print listy #list after removing the first 2 and the last 2 from list if already right position



