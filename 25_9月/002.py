import cmath
a=int(input())
b=int(input())
c=int(input())
x1 = ((-b)+cmath.sqrt(b*b-4*a*c))/(2*a)
x2 = ((-b)-cmath.sqrt(b*b-4*a*c))/(2*a)
def op(x):
    if x.imag != 0:
        print(f'{round(x.real,1)}{"+"if x.imag > 0 else ""}{round(x.imag,1)}i')
    else:
        print(round(x.real,1))

if x1==x2:
    op(x1)
else:
    if x1.imag >= x2.imag:
        op(x1)
        op(x2)
    else:
        op(x2)
        op(x1)
