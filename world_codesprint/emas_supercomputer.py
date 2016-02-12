N, M = [int(x) for x in input().strip().split()]
grid = [[0 for x in range(M)] for x in range(N)]

for i in range(N):
    line = [x for x in input()]
    for j in range(M):
        grid[i][j] = line[j]

