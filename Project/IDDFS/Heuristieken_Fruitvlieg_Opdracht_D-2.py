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
        self.swapsize = 0
        self.pathsize = 0
        if parent:
            self.path = parent.path[:]
            self.path.append(value)
            self.start = parent.start
            self.goal = parent.goal
            self.swapsize = getswapsize(parent.value, self.value)
            self.pathsize += self.swapsize + parent.pathsize
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

def getswapsize(parent, child):
    swapsize = 0
    found = False
    for i in range(len(parent)):
        if (parent[i] != child[i]):
            swapsize += 1
            if (found):
                if (parent[i - 1] == child[i - 1]):
                    swapsize += 1

            found = True
    return swapsize

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
        
    #Method 6:    13 Steps !!!
    def GetDist(self):
        distance = 0
        occured = True
        genome = [0] + copy.copy(self.value) + [len(self.value) + 1]
        for i in range(1, len(self.value) + 2):
            if not (genome[i - 1] == genome[i] - 1 or genome[i - 1] == genome[i] + 1):
                distance += 1
        return distance * 5 + self.pathsize

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
        self.totalswapsize = 0

    def Solve(self):
        start_time = time.time()
        timeout = time.time() + timelimit
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

                    if time.time() > timeout:
                        print "Could not find goal in timelimit"
                        return

                    if child.value == self.goal:
                        self.path = child.path
                        pathsize_score.append(child.pathsize)
                        time_list.append(round(time.time() - start_time, 2))
                        vistited_list.append(len(a.visitedQueue))
                        print "Pathsize =", child.pathsize
                        break
                    self.priorityQueue.put((child.dist,count,child))

        if not self.path:
            print "Goal of ", self.goal, " is not possible for this starting genome!"
        return self.path

if __name__ == '__main__':
    
    timelimit = input("Set timelimit: ")

    ##OUTPUT##
    pathsize_score = []
    time_list = []
    vistited_list =[]

    start_time = time.time()
    
    run_times = input("Set amount of runs: ")
    completed_runs = run_times
    length = input("Set genome length: ")

    for i in range(run_times):
        start1 = random.sample(range(1, length + 1), length)

        goal1 = range(1, len(start1) + 1)

        print start1
        a = AStar_Solver(start1, goal1)
        a.Solve()

        for i in xrange(len(a.path)):
            print " ", i, ")", a.path[i]

        print " "
        print "amount of swaps = ", len(a.path) -1 
        print("--- %s seconds ---" % (time.time() - start_time))
        print "Vistited = ", len(a.visitedQueue)
        

    print ""
    print "Completed genomes =", len(pathsize_score)
    print "TimeLimit was = ", timelimit, "seconds per genome"
    print ""
    print "Path Value/Cost:"
    print ""
    print "Max = ", max(pathsize_score)
    print "Min = ", min(pathsize_score)
    print "Mean = ", sum(pathsize_score) / float(len(pathsize_score))

    print ""
    print "Time (seconds):"
    print ""
    print "Max = ", max(time_list)
    print "Min = ", min(time_list)
    print "Mean = ", sum(time_list) / float(len(time_list))

    print ""
    print "Visited:"
    print ""
    print "Max = ", max(vistited_list)
    print "Min = ", min(vistited_list)
    print "Mean = ", sum(vistited_list) / float(len(vistited_list))

    print ""
    print "pathsize_score: ", pathsize_score
    print ""
    print "time_list: ", time_list
    print ""
    print "vistited_list: ", vistited_list

