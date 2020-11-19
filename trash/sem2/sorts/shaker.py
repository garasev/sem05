import time
import random
from random import *
start_time = time.time()
def shaker(data):	
	up = range(len(data) - 1)		
	while True:
		for indices in (up, reversed(up)):
			swapped = False
			for i in indices:
				if data[i] > data[i+1]:  
					data[i], data[i+1] =  data[i+1], data[i]
					swapped = True
			if not swapped:
				return data
data=[]
for i in range(1000):
        data.append(randint(0,10000))
print(shaker(data))
print("--- %s seconds ---" % (time.time() - start_time))
