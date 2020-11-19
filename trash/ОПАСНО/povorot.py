x=[[1,2,3,4],
   [5,6,7,8],
   [9,10,11,12],
   [13,14,15,16]]


n=4

x = [[x[i] for x in x] for i in range(n)]
for i in range(n):
    x[i].reverse()
for q in x:
    print(q)
x = [[x[i] for x in x] for i in range(n)]
for i in range(n):
    x[i].reverse()
x = [[x[i] for x in x] for i in range(n)]
for i in range(n):
    x[i].reverse()
for q in x:
    print(q)

