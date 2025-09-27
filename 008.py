vc = [[0.08,0.07,0.06],[0.1393,0.1304,0.1087],[0.1349,0.1217,0.1018]]
tx=[[1.1287,1.1127,0.9572],[1.4803,1.2458,1.1243]]
a,b,c,d,e=int(input()),int(input()),int(input()),int(input()),int(input())
plan = [183,383,983]
cost=[]
for i in range(0,3):
    total= int(a*vc[0][i]+b*vc[1][i]+c*vc[2][i]+d*tx[0][i]+e*tx[1][i])
    if plan[i]>total:total=plan[i]
    cost.append((plan[i],total))
cost.sort(key=lambda x:x[-1])
print(cost[0][1])
print(cost[0][0])