# Maak een test-set met 100 random-volgorde genomen van lengte 25. 
# Uncomment de prints.	
# Kan misschien beter, maar werkt. 	

import random
# een random lijst met een lengte van 25
random_list = random.sample(xrange(1, 26), 25)
#print random_list

# hier worden er 100 geprint, misschien niet nodig
for i in range(100):
	n_random_list = random.sample(xrange(1, 26), 25)
	#print n_random_list