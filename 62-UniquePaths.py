
def uniquePaths(m, n):
    path = [[1]*n]*m
    print(path)
    for i in range(1,m):
        for j in range(1,n):
            path[i][j] = path[i-1][j] + path[i][j-1]
    print(path[m-1][n-1])

a = uniquePaths(2,3)
