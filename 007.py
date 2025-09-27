a,b,c = int(input()),int(input()),int(input())
x=a+b
y=b+c
z=a+c
if (a<=0 or b<=0 or c<=0) or not (a<y and b<z and c<x):
    print("Not Triangle")
else:
    if a==b and b==c:
        print("Equilateral Triangle")
    if a==b or b==c or a==c:
        print("Isosceles Triangle")
    sort = sorted([a,b,c],reverse=True)
    a2=sort[0]**2
    b2=sort[1]**2
    c2=sort[2]**2
    if a2 > b2+c2:
        print("Obtuse Triangle")
    if a2 < b2+c2:
        print("Acute Triangle")
    if a2 == b2+c2:
        print("Right Triangle")

