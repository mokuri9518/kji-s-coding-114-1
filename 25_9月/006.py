import math
x,y,z= int(input()),int(input()),int(input())
discount = [[1,0.9,0.85,0.8],[1,0.95,0.85,0.8],[1,0.85,0.8,0.7]]
def count(i):
    if i > 30 :return 3
    elif i >20:return 2
    elif i >10:return 1
    return 0
xp=380*x*discount[0][count(x)]
yp=1200*y*discount[1][count(y)]
zp=180*z*discount[2][count(z)]

print(math.ceil(xp+yp+zp))