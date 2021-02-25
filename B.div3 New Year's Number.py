for _ in range(int(input())):
    n=int(input())
    def chk(n,k):

        if n<2020:
            return "NO"
        while True:
            if n%2020==0:
                if (n/2020)>=k-n:
                    return "YES"
                else:
                    return "NO"

            if n<2020:
                return "NO"
            n-=1
    k=n
    print(chk(n,k))