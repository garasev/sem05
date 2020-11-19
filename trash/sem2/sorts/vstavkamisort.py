#vstavki
import time
import random
from random import *
start_time = time.time()
def insertion(data):
	for i in range(len(data)):
		j = i - 1 
		key = data[i]
		while data[j] > key and j >= 0:
			data[j + 1] = data[j]
			j -= 1
		data[j + 1] = key
	return data
data=[]
for i in range(1000):
        data.append(randint(0,10000))
print(insertion(data))
print("--- %s seconds ---" % (time.time() - start_time))
