n=int(input())
step=input().strip()
矩陣 = [[i * n + j + 1 for j in range(n)] for i in range(n)]
def rotate_right(mat):
    n = len(mat)
    return [[mat[n - j - 1][i] for j in range(n)] for i in range(n)]

def rotate_left(mat):
    n = len(mat)
    return [[mat[j][n - i - 1] for j in range(n)] for i in range(n)]

for _ in step:
    矩陣 = rotate_right(矩陣) if _ == 'R' else rotate_left(矩陣) 

for row in 矩陣:
    print(' '.join(map(str, row)))

