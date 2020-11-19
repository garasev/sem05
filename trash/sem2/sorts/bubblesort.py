import time
import random
from random import *
start_time = time.time()
def bubble(data):
	changed = True
	while changed:
		changed = False
		for i in range(len(data) - 1):
			if data[i] > data[i+1]:
				data[i], data[i+1] = data[i+1], data[i]
				changed = True
	return data
data=[]
for i in range(16):
	data.append(randint(0,15))
print(bubble(data))
print("--- %s seconds ---" % (time.time() - start_time))
