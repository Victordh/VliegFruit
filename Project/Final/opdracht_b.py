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

    def distance_to_goal(self):
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
        self.generation = self.distance_to_goal()

    def distance_to_goal(self):
        """Calculates the distance to the goal. A lower than actual value is
        estimated, to make sure the lowest amount of generations is used."""
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

class BreakpointSolver:
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
        speed = time.time()
        time_out = time.time() + time_limit
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
                    
                    if time.time() > time_out:
                        f.write("-----------------------------------------\n")
                        f.write("Could not find goal within the time limit\n")
                        return
                    
                    if child.genome == self.goal:
                        f.write("-----------------------------------------\n")
                        self.path = child.path
                        self.moved_genes = child.moved_genes
                        amount_of_generations.append(len(self.path) - 1)
                        moved_genes_list.append(self.moved_genes)
                        time_taken.append(round(time.time() - speed, 2))
                        umc_list.append(len(self.unique_mutations_checked))
                        break
                    self.priority_queue.put((child.generation, count,child))
            
        if not self.path:
            print ("Goal of ", self.goal,
                  " is not possible for this starting genome!")
        return self

def main():
    """Finds the smallest amount of generations between
    100 random genomes and the genome of Drosophila Miranda"""
    
    total_speed = time.time()
    
    for i in range(100):
        start_1 = random.sample(range(1, 26), 25)
        goal_1 = range(1, len(start_1) + 1)
        
        solver = BreakpointSolver(start_1, goal_1)
        solver.solve()
        
        for i in xrange(len(solver.path)):
            if i < 10:
                f.write(" ")
            f.write(str(i) + ") " + str(solver.path[i]) + "\n")
        
        f.write("\n   Amount of generations: " + str(len(solver.path) - 1) +
                "\n")
        f.write("             Moved genes: " + str(solver.moved_genes) + "\n")
        f.write("Unique mutations checked: " +
                str(len(solver.unique_mutations_checked)) + "\n")
        f.write("   Time taken in seconds: %.2f" % (time.time() - total_speed)
                + "\n")
        
    f.write("\n\nCompleted genomes: " + str(len(amount_of_generations)))

    f.write("\n\nAmount of generations:\n")
    f.write(" Max: " + str(max(amount_of_generations)) + "\n")
    f.write(" Min: " + str(min(amount_of_generations)) + "\n")
    f.write("Mean: " + str((round(sum(amount_of_generations) /
                       float(len(amount_of_generations)), 2))))
    
    f.write("\n\nAmount of moved genes:\n")
    f.write(" Max: " + str(max(moved_genes_list)) + "\n")
    f.write(" Min: " + str(min(moved_genes_list)) + "\n")
    f.write("Mean: " + str((round(sum(moved_genes_list) /
                       float(len(moved_genes_list)), 2))))

    f.write("\n\nTime taken (in seconds):\n")
    f.write(" Max: " + str(max(time_taken)) + "\n")
    f.write(" Min: " + str(min(time_taken)) + "\n")
    f.write("Mean: " + str(round(sum(time_taken) /
                       float(len(time_taken)), 2)))

    f.write("\n\nUnique mutations checked:\n")
    f.write(" Max: " + str(max(umc_list)) + "\n")
    f.write(" Min: " + str(min(umc_list)) + "\n")
    f.write("Mean: " + str(round(sum(umc_list) /
                       float(len(umc_list)), 2)))

    f.write("\n\n")
    f.write("List of amount of generations:\n" + str(amount_of_generations)
            + "\n")
    f.write("List of amount of moved genes:\n" + str(moved_genes_list) + "\n")
    f.write("List of time taken:\n" + str(time_taken) + "\n")
    f.write("List of amount of unique mutations checked:\n" +
            str(umc_list))

if __name__ == '__main__':
    time_limit = 1800
    amount_of_generations = []
    moved_genes_list = []
    time_taken = []
    umc_list = [] # umc = unique mutations checked
    
    f = open('output_b.txt', 'w')
    f.write("Time limit in seconds: " + str(time_limit) + "\n")
    main()
    f.close()
