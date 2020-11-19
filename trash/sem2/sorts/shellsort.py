import time
import random
m = []
for i in range(1000):
    m.append(random.randint(0,10000))
m1 = m[:]
a = sorted(m[:])
#print(m)
start_time = time.time()
d = len(m)
while d != 1:
    d //= 2
    start = -1
    while start != d - 1:
        start += 1
        for j in range(start + d, len(m), d):
            ind = j
            for z in range(j, start - 1, -d):
                if m[ind] < m[z]:
                    m[ind], m[z] = m[z], m[ind]
                    ind = z
print("--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()
#print(m)
for i in range(len(m1) - 1):
    indx = i
    for j in range(i + 1, len(m1)):
        if m1[j] < m1[indx]:
            indx = j
    m1[i], m1[indx] = m1[indx], m1[i]
print("--- %s seconds ---" % (time.time() - start_time))
