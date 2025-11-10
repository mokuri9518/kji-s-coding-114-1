table = [0 for _ in range(9)]
m = input()
steps = map(int,input().split())
for s in steps:
    table[s-1] = m
    m = '2' if m == '1' else '1'
for i in range(3):
    for j in range(3):
        print(table[3*i+j],end=" ")
    print()
result = "Undecided"
players = {'1': 'Player', '2': 'Computer'}
for i in range(3):
    if table[3*i] == table[3*i+1] == table[3*i+2] != 0:
        result = f"{players[table[3*i]]} win"
    if table[i] == table[i+3] == table[i+6] != 0:
        result = f"{players[table[i]]} win"
if table[0] == table[4] == table[8] != 0:
    result = f"{players[table[0]]} win"
if table[2] == table[4] == table[6] != 0:
    result = f"{players[table[2]]} win"
print(result)
