from Queue import PriorityQueue
import string
import random
import copy
import sys
import math
import time


class FruitFly(object):
    """A fruit fly with a certain genome and references to
    previous and future generations."""
    def __init__(self, genome, parent, start = 0, goal = 0):
        self.children = []
        self.genome = genome
        self.parent = parent
        self.generation = 0
        
        if parent:
            self.path = parent.path[:]
            self.path.append(genome)
            self.start = parent.start
            self.goal = parent.goal
        else:
            self.path = [genome]
            self.start = start
            self.goal = goal

    def get_generation(self):
        pass

    def create_children(self):
        pass

def mutation(size, pos, genome):
    """Reverses a piece of size, starting at position, in a genome."""
    piece = []
    count = 0
    while count < size:
        piece.append(genome[count + pos])
        count += 1
    piece.reverse()
    count = 0
    while count < size:
        genome[count + pos] = piece[count]
        count += 1
    return genome

class FruitFlyMutation(FruitFly):
    """A next generation of a fruit fly, with a mutated genome."""
    def __init__(self, genome, parent, start = 0, goal = 0):
        super(FruitFlyMutation, self).__init__(genome, parent, start, goal)
        self.generation = self.get_generation()
    
    def get_generation(self):
        """Keeps track of the amount of generations."""
        generation = 0
        genome = [0] + copy.copy(self.genome) + [len(self.genome) + 1]

        for i in range(1, len(self.genome) + 2):
            if not (genome[i - 1] == genome[i] - 1 or
                    genome[i - 1] == genome[i] + 1):
                generation += 1
            
        return generation + len(self.path)

    def create_children(self):
        """Creates all possible mutations of the next generation."""
        if not self.children:
            for i in range(2, len(self.genome) + 1):
                for j in xrange(len(self.goal) - i + 1):
                    genome = copy.copy(self.genome)
                    mutated_genome = mutation(i, j, genome)
                    child = FruitFlyMutation(mutated_genome, self)
                    self.children.append(child)

class AStarSolver:
    """Solver that finds the smallest amount of generations needed to get from
    one fruit fly to one with a different genome"""
    def __init__(self, start, goal):
        self.path = []
        self.visited_queue = []
        self.priority_queue = PriorityQueue()
        self.start = start
        self.goal = goal

    def solve(self):
        fruit_fly = FruitFlyMutation(self.start, 0, self.start, self.goal)
        count = 0
        self.priority_queue.put((0, count, fruit_fly))
        while (not self.path and self.priority_queue.qsize()):
            closest_child = self.priority_queue.get()[2]
            closest_child.create_children()
            self.visited_queue.append(closest_child.genome)
            for child in closest_child.children:
                if child.genome not in self.visited_queue:
                    count +=1
                    if child.genome == self.goal:
                        self.path = child.path
                        break
                    self.priority_queue.put((child.generation, count,child))

        if not self.path:
            print ("Goal of ", self.goal,
                  " is not possible for this starting genome!")
        return self.path

def main():
    """Finds the smallest amount of generations between
    Drosophila Melanogaster and Drosophila Miranda"""
    speed = time.time()
    
    start_1 = [23, 1, 2, 11, 24, 22, 19, 6, 10, 7, 25, 20, 5, 8, 18, 12, 13,
               14, 15, 16, 17, 21, 3, 4, 9]
    goal_1 = range(1, len(start_1) + 1)
    print start_1

    a = AStarSolver(start_1, goal_1)
    a.solve()
    for i in xrange(len(a.path)):
        print " ", i, ")", a.path[i]

    print " "
    print "Amount of swaps:", len(a.path) - 1 
    print "Visited:        ", len(a.visited_queue)
    print("--- %s seconds ---" % (time.time() - speed))
    

if __name__ == '__main__':
    main()
