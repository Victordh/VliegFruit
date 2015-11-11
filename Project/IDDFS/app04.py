#Creates a class node
class Node(object):
	def __init__(self, current):
		self.current = current;    # a.k.a name or value
		self.neighbours = []; 	 
		self.visited = False;
		self.steps = 0;

# Depth First Search function
def dfs(node, limitDepth, currentDepth):

	# What to look for?
	goal = "D";
	# If currentDepth is 0 there wont be a search
	if (currentDepth <= 0):
		return;

	node.visited = True;
	print("%s ->" % node.current);

	# Iterates over all of the neighbour values of the current node
	for n in node.neighbours:

		if not n.visited:
			# Check if this is what we are looking for
			if (n.current == goal):
				print("Found with %s step(s)" % n.steps);
				return limitDepth - 1;
			# Recalls itself to go deeper in the tree 
			dfs(n, limitDepth, currentDepth);
	#This is returned to set a new limit on the last (and so shorted) solution
	return limitDepth;

def iterativeDeepeningDepthFirstSearch(node, limitDepth, currentDepth):
	#While the current depth < the limited depth do:
	while(currentDepth < limitDepth):
		print("limitDepth = %s" % limitDepth)
		limitDepth = dfs(node, limitDepth, currentDepth);
		
		currentDepth += 1;

node1 = Node("A");

node2 = Node("B");
node3 = Node("C");
node4 = Node("D"); 	 # This is a goal we find last.

node5 = Node("E");
node6 = Node("F");
node7 = Node("G");

node8 = Node("H");
node9 = Node("I");
node10 = Node("D");  # This is the goal we find second

node11 = Node("K");  #
node12 = Node("L");  # These values will be ignored by the search, because we already found a soluction on this level in the tree
node13 = Node("M");  #

node14 = Node("D")   # This is the goal we find first

# node1 = Node(123);

# node2 = Node(213);
# node3 = Node(132);
# node4 = Node(321);

# node5 = Node(123);
# node6 = Node(231);
# node7 = Node(312);

# node8 = Node(312);
# node9 = Node(123);
# node10 = Node(321);

# node11 = Node(231);
# node12 = Node(312);
# node13 = Node(123);

# node14 = Node(123)

#Index for which layer a node is in the tree.
node1.steps = (0);
node2.steps = (1);
node3.steps = (1);
node4.steps = (1);
node5.steps = (2);
node6.steps = (2);
node7.steps = (2);
node8.steps = (2);
node9.steps = (2);
node10.steps = (2);
node11.steps = (2);
node12.steps = (2);
node13.steps = (2);
node14.steps = (3);

# Creates neighbours of nodes (our test tree)
node1.neighbours.append(node2);
node1.neighbours.append(node3);
node1.neighbours.append(node4);

node2.neighbours.append(node5);
node2.neighbours.append(node6);
node2.neighbours.append(node7);

node3.neighbours.append(node8);
node3.neighbours.append(node9);
node3.neighbours.append(node10);

node4.neighbours.append(node11);
node4.neighbours.append(node12);
node4.neighbours.append(node13);

node6.neighbours.append(node14);

# Calls the search function
iterativeDeepeningDepthFirstSearch(node1, 2, 1)
