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
        self.moved_genes = 0
        
        if parent:
            self.path = parent.path[:]
            self.path.append(genome)
            self.start = parent.start
            self.goal = parent.goal
            self.moved_genes = (get_moved_genes(parent.genome, self.genome) +
                                parent.moved_genes)
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

def get_moved_genes(parent, child):
    """Calculates the amount of moved genes in a mutation."""
    moved_genes = 0
    found_mutation = False
    for i in range(len(parent)):
        if parent[i] != child[i]:
            moved_genes += 1
            
            # makes sure equal values in the middle of a mutation of odd
            # length is counted
            if (found_mutation):
                if parent[i - 1] == child[i - 1]:
                    moved_genes += 1
            found_mutation = True
    return moved_genes

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
            
        #return generation + len(self.path)         # opdracht A
        return generation * 5 + self.moved_genes    # opdracht C

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
        self.unique_mutations_checked = []
        self.priority_queue = PriorityQueue()
        self.start = start
        self.goal = goal
        self.moved_genes = 0

    def solve(self):
        fruit_fly = FruitFlyMutation(self.start, 0, self.start, self.goal)
        count = 0
        self.priority_queue.put((0, count, fruit_fly))
        while (not self.path and self.priority_queue.qsize()):
            closest_child = self.priority_queue.get()[2]
            closest_child.create_children()
            self.unique_mutations_checked.append(closest_child.genome)
            for child in closest_child.children:
                if child.genome not in self.unique_mutations_checked:
                    count +=1
                    if child.genome == self.goal:
                        self.path = child.path
                        self.moved_genes = child.moved_genes
                        break
                    self.priority_queue.put((child.generation, count,child))

        if not self.path:
            print ("Goal of ", self.goal,
                  " is not possible for this starting genome!")
        return self

def main():
    """Finds the smallest amount of moved genes between
    Drosophila Melanogaster and Drosophila Miranda"""
    speed = time.time()
    
    start_1 = [23, 1, 2, 11, 24, 22, 19, 6, 10, 7, 25, 20, 5, 8, 18, 12, 13,
               14, 15, 16, 17, 21, 3, 4, 9]
    goal_1 = range(1, len(start_1) + 1)
    print start_1

    f = open('output_c.txt', 'w')
    
    a = AStarSolver(start_1, goal_1)
    a.solve()
    for i in xrange(len(a.path)):
        print " ", i, ")", a.path[i]
        f.write(str(i) + ") " + str(a.path[i]) + "\n")

    print " "
    print "----------------------------------------"
    print " "
    print "   Amount of generations:", len(a.path) - 1
    print "             Moved genes:", a.moved_genes
    print "Unique mutations checked:", len(a.unique_mutations_checked)
    print("              Time taken: %.2f seconds" % (time.time() - speed))
    
    f.write("----------------------------------------\n")
    f.write("   Amount of generations: " + str(len(a.path) - 1) + "\n")
    f.write("             Moved genes: " + str(a.moved_genes) + "\n")
    f.write("Unique mutations checked: " + str(len(a.unique_mutations_checked)) + "\n")
    f.write("              Time taken: %.2f seconds" % (time.time() - speed))
    
    f.close()

if __name__ == '__main__':
    main()
