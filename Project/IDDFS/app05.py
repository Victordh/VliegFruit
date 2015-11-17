import random

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


def move(count, genome, l_goal, bound, visited):
	if count >= bound:
		return False

	# Het interval op range is een beperking van de maximale swap "size"
	for i in range(2, 4): #len(genome) + 1   <<=== de "normale" range

		for j in range(len(genome) - i + 1):
			new_genome = swap(i, j, list(genome))

			if genome == l_goal:
				print "answer", count + 1
				return True

			if new_genome in visited:
				continue

			visited.append(genome)
			res = move(count + 1, new_genome, l_goal, bound, visited)

			if res:
				return res
	return False


def solve():
	count = 0
	# Is het aantal getallen in de lijst "genome", moet nog effe wat netter zodat hij meteen uit genome gehaald word, maar ik krijg steeds een indent error ofzo.
	k = 5

	genome = [3, 4, 2, 5, 1] 

	# Ons genome
	# genome = [23, 1, 2, 11, 24, 22, 19, 6, 10, 7, 25, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9] 

	# random genome van lengte k
	# genome = random.sample(range(1, k + 1), k)

	# Genereert het eind doel gebaseerd op de lengte van lijst "genome" [1, 2, 3, 4 ,5]
	l_goal = range(1, k + 1)

	# Sum range k is maximale diepte dat een oplossing zou moeten zitten. Dit limit kun je bijv vervangen door: for i in range(2) voor een maximale diepte van 2
	for i in range(sum(range(k))):
		visited = []
		if move(count, genome, l_goal, i, visited):
			break


solve()
