from Queue import PriorityQueue
import string
import random
import copy
import sys
import math
import time

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

class State_String(State):
    def __init__(self,value,parent,start = 0,goal = 0):
        super(State_String,self).__init__(value,parent,start,goal)
        self.dist = self.GetDist()
    
        #Method 6:    13 Steps !!!
    def GetDist(self):
        distance = 0
        occured = True
        genome = [0] + copy.copy(self.value) + [len(self.value) + 1]

        for i in range(1, len(self.value) + 2):
            if not (genome[i - 1] == genome[i] - 1 or genome[i - 1] == genome[i] + 1):
                distance += 1

        return distance + len(self.path)

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
    start_time = time.time()
    
    start1 = [23, 1, 2, 11, 24, 22, 19, 6, 10, 7, 25, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9]

    print start1
    goal1 = range(1, len(start1) + 1)

    a = AStar_Solver(start1, goal1)
    a.Solve()
    for i in xrange(len(a.path)):
        print " ", i, ")", a.path[i]

    print " "
    print "amount of swaps = ", len(a.path) -1 
    print("--- %s seconds ---" % (time.time() - start_time))
    print "Vistited = ", len(a.visitedQueue)
