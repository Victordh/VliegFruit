import global_variables
import random

# swaps in genome [genome] the position of the [size] amount of numbers
# starting on position [pos]
def swap(size, pos, genome):
    global_variables.counter += 1
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

# takes a genome and returns it with part of random size at random position
# inverted
def random_inversion(genome):
    random_size = random.randint(2,len(genome))
    random_pos = random.randint(0, len(genome) - random_size)
    return swap(random_size, random_pos, genome)

# takes a genome and returns the calculated index (the sum of the distance of
# each gen to its correct place)
def sum_distance_correct_spot(genome):
    sum = 0
    for i in range(len(genome)):
        temp = abs(genome.index(i + 1) - i)
        sum += temp
    return sum

# calculates the sum of the distance between each gen and the neighbours it is
# supposed to have
def sum_distance_neighbours(genome):
    sum = 0
    for i in range(len(genome)):
        if i == 0:
            temp = abs(genome.index(i + 1) - genome.index(i + 2))
        elif i == (len(genome) - 1):
            temp = abs(genome.index(i + 1) - genome.index(i))
        else:
            temp = abs(genome.index(i + 1) - genome.index(i))
            temp += abs(genome.index(i + 1) - genome.index(i + 2))
        sum += temp
    return sum

#def shorten_genome(genome):
    # if numbers are already on the correct spot (only at start or end),
    # make the genome shorter and use the shorter one instead
