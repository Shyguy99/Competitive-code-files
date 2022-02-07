n=10
dp = [1]
i = j = k = 0

for l in range(n):
    pi, pj, pk = dp[i] * 2, dp[j] * 3, dp[k] * 5

    m = min(pi, pj, pk)
    dp.append(m)
    if pi == m:
        i += 1
    if pj == m:
        j += 1
    if pk == m:
        k += 1
print(dp)
print(dp[n - 1])