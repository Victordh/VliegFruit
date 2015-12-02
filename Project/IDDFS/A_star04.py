from Queue import PriorityQueue
import string
import random
import copy
import sys
import math

class State(object):
    def __init__(self,value,parent,start = 0,goal = 0):
        self.children = []
        self.value = value
        self.parent = parent
        self.dist = 0
        if parent:
            self.path = parent.path[:]
            self.path.append(value)
            self.start = parent.start
            self.goal = parent.goal
        else:
            self.path = [value]
            self.start = start
            self.goal = goal


    def GetDist(self):
        pass

    def CreateChildren(self):
        pass

def swap(size, pos, genome):
    y = []
    count = 0
    while count < size:
        y.append(genome[count + pos])
        count += 1
    y.reverse()
    count = 0
    while count < size:
        genome[count + pos] = y[count]
        count += 1
    return genome

def f1(genome):
    import copy
    i = 0
    tmp_genome = copy.copy(genome)
    while True:
        p0  = tmp_genome[0]
        if p0 == 1: break
        #print tmp_genome[:p0][::-1]
        tmp_genome[:p0] = tmp_genome[:p0][::-1]
        i  += 1
    return i

def checkFor(self):
    
    #print self.value
    if self.value[12] != 13:
        return 48
    if self.value[11] != 12:
        return 24

    if self.value[13] != 14:
        return 24


        # elif self.value[24] == 25:
        #     if self.value[1] != 2:
        #         return 12
    return 0

def check_neighbours(genome):
    i = 1
    distance = 0
    while( i < len(genome)):

        if (genome.index(i) != genome.index(i + 1) -1):
            distance += 1
        i += 1
    #print distance
    return distance

class State_String(State):
    def __init__(self,value,parent,start = 0,goal = 0):
        super(State_String,self).__init__(value,parent,start,goal)
        self.dist = self.GetDist()

    # Heuristics to guess the path length
    # def GetDist(self):
    #     if self.value == self.goal:
    #         return 0
    #     dist = 0            # The sum of the distance of all numbers to their goal 
    #     dist_rev = 1       # The sum of the distance of all numbers to their negative goal position 
    #     # n_dist = 0
    #     # n_dist_rev = 0
    #     for i in range(len(self.goal)):
    #         gen = self.goal[i]

    #         if self.value.index(gen) != i:
    #             dist += 1
    #         # dist += abs(i - self.value.index(gen))
    #         # dist_rev += abs((len(self.value) - 1 - i) - self.value.index(gen))

    #         # n_dist = dist
    #         # n_dist_rev = dist_rev

    #         # if (gen == self.value[i] + 1 or gen == self.value[i] - 1) :
    #         #     n_dist -= 1
    #         #     n_dist_rev -= 1
                
    #         # print "gen =", gen
    #         # print self.value[i] + 1
    #         # print self.value[i] - 1
    #         # print self.value


    #     #return min(math.sqrt(dist * dist), math.sqrt(dist_rev * dist_rev))
    #     #print math.floor(math.sqrt((dist) + (dist_rev)))
    #     #print self.value
    #     #return math.floor(math.sqrt((dist) + (dist_rev))- 18)

    #     return len(self.path) + dist#min(dist, dist_rev)
    # Method 5: 

    #Method 1: 22 steps
    # def GetDist(self):
    #     if self.value == self.goal:
    #         return 0
    #     dist = 0            # The sum of the distance of all numbers to their goal 
    #     dist_rev = 1       # The sum of the distance of all numbers to their negative goal position 
    #     for i in range(len(self.goal)):
    #         gen = self.goal[i]
    #         dist += abs(i - self.value.index(gen))  #+ f1(self.value) #+ checkFor(self.value)
    #         dist_rev += abs((len(self.value) - 1 - i) - self.value.index(gen)) #+ f1(self.value) #+ checkFor(self.value) 
    #         #dist_rev = 100000


    #     return min(dist, dist_rev) + len(self.path)

    #Method 2: 25 steps
    # def GetDist(self):
    #     if self.value == self.goal:
    #         return 0
    #     dist = 0            # The sum of the distance of all numbers to their goal 
    #     dist_rev = 1       # The sum of the distance of all numbers to their negative goal position 
    #     for i in range(len(self.goal)):
    #         gen = self.goal[i]
    #         dist += abs(i - self.value.index(gen))
    #         dist_rev += abs((len(self.value) - 1 - i) - self.value.index(gen))

    #     count = 0
    #     count_rev = 1
    #     for i in range(len(self.goal) / 2):
    #         index1 = int(len(self.goal) / 2) + i
    #         index2 = int(len(self.goal) / 2) - i
    #         if self.value[index1] == index1 + 1:
    #             count += 2
    #         if self.value[index2] == index2 + 1:
    #             count_rev += 2

    #     return min(dist, dist_rev) - min(count, count_rev) + len(self.path)


    #Method 3: 24 steps
    # def GetDist(self):
    #     if self.value == self.goal:
    #         return 0
    #     x_dist = 0            # The sum of the distance of all numbers to their goal 
    #     x_dist_rev = 1       # The sum of the distance of all numbers to their negative goal position 
    #     y_dist = 0
    #     y_dist_rev = 1
    #     for i in range(len(self.goal) - 1):
    #         if self.value[i] > self.value[i+1]:
    #             x_dist += 1

    #         if self.value[i] < self.value[i+1]:
    #             x_dist_rev += 1
    #     for i in range(len(self.goal)):
    #         gen = self.goal[i]
    #         y_dist += abs(i - self.value.index(gen))
    #         y_dist_rev += abs((len(self.value) - 1 - i) - self.value.index(gen))

    #     #print min(math.sqrt(x_dist * x_dist + y_dist * y_dist), math.sqrt(x_dist_rev * x_dist_rev + y_dist_rev * y_dist_rev)) + len(self.path)
    #     #print self.value
    #     #print len(self.path)
    #     return min(math.sqrt(x_dist * x_dist + y_dist * y_dist), math.sqrt(x_dist_rev * x_dist_rev + y_dist_rev * y_dist_rev)) + len(self.path)

""" Brain storm 

 [3, 1, 2]   3   2

 [1, 3, 2]   2   1
 [3, 2, 1]   2   1
 [2, 1, 3]   2   1

 [3, 4, 1, 2]    4   2

 [4, 3, 1, 2]    4   3
 [3, 1, 4, 2]    4   3  
 [3, 4, 2, 1]    4   2   
 [1, 4, 3, 2]    2   1
 [3, 2, 1, 4]    2   1
 [2, 1, 4, 3]    4   2

"""



        #Method 4: 19 steps
    def GetDist(self):
        print self.value
        if self.value == self.goal:
            return 0
        dist = 0            # The sum of the distance of all numbers to their goal 
        dist_rev = 1       # The sum of the distance of all numbers to their negative goal position 
        for i in range(len(self.goal)):
            gen = self.goal[i]
            dist += abs(i - self.value.index(gen)) + f1(self.value) #+ check_neighbours(self.value)
            dist_rev += abs((len(self.value) - 1 - i) - self.value.index(gen))  + f1(self.value) #+ check_neighbours(self.value)



        return min(dist, dist_rev) + len(self.path)

    def CreateChildren(self):
        if not self.children:
            for i in range(2, len(self.value) + 1):
                for j in xrange(len(self.goal) - i + 1):
                    val = copy.copy(self.value)
                    val = swap(i, j, val)
                    child = State_String(val,self)
                    self.children.append(child)


class AStar_Solver:
    def __init__(self,start,goal):
        self.path = []
        self.visitedQueue = []
        self.priorityQueue = PriorityQueue()
        self.start = start
        self.goal = goal

    def Solve(self):
        startState = State_String(self.start,0,self.start,self.goal)
        count = 0
        self.priorityQueue.put((0,count,startState))
        while(not self.path and self.priorityQueue.qsize()):
            closestChild = self.priorityQueue.get()[2]
            closestChild.CreateChildren()
            self.visitedQueue.append(closestChild.value)
            for child in closestChild.children:
                if child.value not in self.visitedQueue:
                    count +=1
                    if child.value == self.goal:
                        self.path = child.path
                        break
                    self.priorityQueue.put((child.dist,count,child))

        if not self.path:
            print "Goal of ", self.goal, " is not possible for this starting genome!"
        return self.path

if __name__ == '__main__':
    
    # Generate a random list for start.
    length = 25
    #start1 = random.sample(range(1, length + 1), length)

    # Manual input of a list
    #start1 = [23, 1, 2, 11, 24, 22, 19, 6, 10, 7, 25, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9]
    start1 = [3, 4, 2, 1]
    #print "    )", start1
    goal1 = range(1, len(start1) + 1)

    a = AStar_Solver(start1, goal1)
    a.Solve()
    for i in xrange(len(a.path)):
        print " ", i, ")", a.path[i]

    print " "
    print "amount of swaps = ", len(a.path) -1 
