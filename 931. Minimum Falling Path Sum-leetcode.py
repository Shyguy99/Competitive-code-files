
def tra(i, j, dp):
    global ar
    global n
    if j < 0 or j > n - 1:
        return 100000000000

    if i == n - 1:
        return ar[i][j]
    if dp[i][j] != -1: return dp[i][j]
    dp[i][j] = ar[i][j] + min(tra(i + 1, j - 1, dp), tra(i + 1, j, dp), tra(i + 1, j + 1, dp))
    return dp[i][j]

ar = matrix[:]
n = len(matrix)
m = 1000000000000000
dp = [[-1 for i in range(n)] for j in range(n)]
for i in range(n):
    m = min(m, tra(0, i, dp))
return m