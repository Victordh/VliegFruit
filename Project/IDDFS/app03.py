class Node(object):
	def __init__(self, current):
		self.current = current;
		self.neighbours = [];
		self.visited = False;

def dfs(node, maxDepth):

	if (maxDepth <= 0):
		return;

	node.visited = True;
	print("%s ->" % node.current);

	for n in node.neighbours:
		if not n.visited:
			dfs(n, maxDepth);


# / Recurse for all children of node.
#     for (var i=0, c=node.children.length; i<c; i++) {
#         depthFirstSearch(node.children[i], maxDepth-1);
#     }



def iterativeDeepeningDepthFirstSearch(node):
	totalDepth = 2;
	maxDepth = 1;
	
	while(maxDepth < totalDepth):
		dfs(node, maxDepth);
		maxDepth += 1;

		


node1 = Node("A");

node2 = Node("B");
node3 = Node("C");
node4 = Node("D");

node5 = Node("E");
node6 = Node("F");
node7 = Node("G");

node8 = Node("H");
node9 = Node("I");
node10 = Node("J");

node11 = Node("K");
node12 = Node("L");
node13 = Node("M");

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


#dfs(node1);

iterativeDeepeningDepthFirstSearch(node1)
