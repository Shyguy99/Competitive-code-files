n=int(input())

def tra(n,dp):
    print(n)
    if n==2:
        return 2
    if n==1 or n==0:
        return 1

    if dp[n]!=-1: return dp[n]
    s=0
    for i in range(1,n+1):

        s+=tra(i-1,dp)*tra(n-i,dp)
    dp[n]= s
    return s
dp=[-1]*(n+1)
print(tra(n,dp))