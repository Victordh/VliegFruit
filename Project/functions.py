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

genome = [[1], [2], [3], [5], [6], [4], [7], [9], [8], [10]]
genome2 = [[5], [4], [3], [1], [2], [8], [10], [9], [6], [7]]

# takes a genome and returns it with neighbours that should be next to
# eachother merged
def merge_correct_neighbours(genome, i):
    better = list(genome)
    if i < (len(genome) - 1):
        # merges if element on the right is 1 higher than current element
        if (genome[i][len(genome[i]) - 1] == genome[i + 1][0] - 1):
            genome[i] = genome[i] + genome[i + 1]
            genome.pop(i + 1)
            merge_correct_neighbours(genome, i)
        # merges if element on the right is 1 lower than current element
        elif(genome[i][len(genome[i]) - 1] == genome[i + 1][0] + 1):
            genome[i] = genome[i] + genome[i + 1]
            genome.pop(i + 1)
            merge_correct_neighbours(genome, i)
        # moves to the next element
        else:
            merge_correct_neighbours(genome, i + 1)
    return genome

# better = list(genome)
# print better
# print genome[0][len(genome[0]) - 1]
# print genome[0 + 1][0]
# print genome[1][len(genome[1]) - 1]
# print genome[1 + 1][0]
# better[0] = genome[0] + genome[1]
# print better
# better.pop(1)
# print better
print merge_correct_neighbours(genome, 0)
print merge_correct_neighbours(genome2, 0)

#def shorten_genome(genome):
    # if numbers are already on the correct spot (only at start or end),
    # make the genome shorter and use the shorter one instead
