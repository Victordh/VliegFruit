class Node(object):
	def __init__(self, current):
		self.current = current;
		self.neighbours = [];
		self.visited = False;

def dfs(node):

	node.visited = True;
	print("%s ->" % node.current);

	for n in node.neighbours:
		if not n.visited:
			dfs(n);


node1 = Node(123);

node2 = Node(213);
node3 = Node(132);
node4 = Node(321);

node5 = Node(123);
node6 = Node(231);
node7 = Node(312);

node8 = Node(312);
node9 = Node(123);
node10 = Node(321);

node11 = Node(231);
node12 = Node(312);
node13 = Node(123);




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


dfs(node1);

