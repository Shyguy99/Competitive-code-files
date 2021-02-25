for _ in range(int(input())):
    n=int(input())
    b=n+1
    def tra(i,b,dp):
        if i>b:
            return 0
        if i==b:
            return 1
        if dp[i]==-1:

            o=tra(i+1,b,dp)
            p=  tra(i+2,b,dp)

            q=tra(i+3,b,dp)

            dp[i]=o+p+q

            return dp[i]
        else:
            return dp[i]
    dp=[-1 for i in range(n+1)]

    print(tra(0,b,dp))