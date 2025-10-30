lens = [0 for _ in range(-20,21)]
sum:int = 0
for i in range(1,4):
    x1=int(input())
    x2=int(input())
    for i in range(x1,x2):
        lens[i+20] = 1
for i in lens:
    sum += i

print(sum)

