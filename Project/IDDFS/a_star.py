import copy

class Goal:
      import random
      def __init__(self):
         self.genome = []

      def set_random_goal(self, size):
         self.genome = random.sample(range(1, size + 1), size)

      def set_goal(self, size):
         self.genome = range(1, size + 1)

class Node(object):
	def __init__(self, genome):
		self.genome = genome;    # a.k.a name or value  
		self.neighbours = [];
		self.neighbours_count = 0
		self.parent = None
		self.g_score = 0
		self.f_score = 0

	def create_neighbours(self):
		for i in range(2, 4): #len(self.genome) + 1
			for j in range(len(self.genome) - i + 1):
				new_node = Node(swap(i, j, copy.copy(self.genome)))
				new_node.parent = self
				new_node.g_score = self.g_score + 1
				self.neighbours.append(new_node)
				self.neighbours_count += 1

	def index_of(genome):
		index = 0
		for i in range(len(genome)):
			temp = abs(genome.index(i + 1) - i)
			index += temp
		return index

def calculate_path(node):
	while node.parent != None:
		print node.genome
		node = node.parent

def A_star(start,goal):

	closedset = []
	openset = []
	openset.append(start)

	start.g_score = 0
	start.f_score = start.g_score + 2 #heuristic_cost_estimate(start, goal)

	while openset is not None:
		current = lowest_f(openset) #the node in OpenSet having the lowest f_score[] value
		#print "current genome =", current.genome
		#print "goal genome =", goal.genome
		if (current.genome == goal.genome):
			return calculate_path(current)

		openset.remove(current)
		closedset.append(current)
		for n in current.neighbours:
			if (n in closedset):	
				continue		# Ignore the neighbor which is already evaluated.
			tentative_g_score = current.g_score + 1 # length of this path.

			if (n not in openset):	# Discover a new node
				openset.append(n)

			elif (tentative_g_score >= n.g_score):
				continue		# This is not a better path.

            ## This path is the best until now. Record it!
            #Came_From[neighbor] = current.genome
            #g_score[neighbor] := tentative_g_score
            #f_score[neighbor] := g_score[neighbor] + heuristic_cost_estimate(neighbor, goal)
	return False


def lowest_f(openset):
	lowest = None
	for node in openset:
		print node.g_score
		print node.genome
		if (lowest == None):
			lowest = node
		if (node.f_score < lowest.f_score):
			lowest = node
	#print lowest.genome
	return lowest

def swap(size, pos, genome):
    y = []
    count = 0
    while count < size:
        y.append(genome[count + pos])
        count += 1
    #print y
    y.reverse()
    #print y
    count = 0
    while count < size:
        genome[count + pos] = y[count]
        count += 1
    return genome

goal = Goal()
goal.set_goal(4)
#print goal.genome

start = Node([3, 4, 1, 2])
start.create_neighbours()
#print start.neighbours

#print start.genome

A_star(start, goal)