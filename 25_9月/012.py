dic = {"J":0.5,"Q":0.5,"K":0.5,"A":1}
for i in range(2,11):
    dic.update({f'{i}':i})

x =[input(),input(),input()]
y =[input(),input(),input()]
xv=0
yv=0
for card in x:
    xv+=dic[card]
for card in y:
    yv+=dic[card]
xv = 0 if xv>10.5 else xv
yv = 0 if yv>10.5 else yv
print(int(xv) if int(xv)==xv else xv)
print(int(yv) if int(yv)==yv else yv)
if xv==yv:
    print("Tie")
elif xv>yv:
    print('X Win')
elif xv<yv:
    print('Y Win')
else:print("???")