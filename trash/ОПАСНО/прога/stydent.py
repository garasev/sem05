from math import*

N=int(input('Введите кол-во студентов в очереди N<=50: '))
t=[0]*N
print('Введите время обслуживания каждого студента в столбец ')
for i in range(N):
    t[i]=float(input('Время обслуживания: '))
c=[0]*N
mint=t[0]
nt=0
for i in range(N):
    c[i]=c[i-1]+t[i]
    if mint>t[i]:
        nt=i
        mint=t[i]
print('Наименьшее время обслуживания',mint,'это был студент №',nt+1)
print('Время ожидания каждого из студента: ',c)
    
