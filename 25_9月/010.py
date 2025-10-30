from math import ceil
a = list(map(int,input().split(' ')))
b = list(map(int,input().split(' ')))
c = list(map(int,input().split(' ')))
a.insert(1,100)
b.insert(1,100)
c.insert(1,100)
def count(i):
    if i > 30 :return 3
    elif i >20:return 2
    elif i >10:return 1
    return 0
def discount(x):
    return x[1:5][count(x[0])]*0.01*x[0]
P = [[380*discount(a),'A'],[1200*discount(b),'B'],[180*discount(c),'C']]
Ma = max(P,key=lambda x:x[0])
Mi = min(P,key=lambda x:x[0])
print(f'{Ma[1]}: {ceil(Ma[0])}')
print(f'{Mi[1]}: {ceil(Mi[0])}')
print(sum(ceil(x[0]) for x in P))