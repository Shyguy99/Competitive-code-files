for _ in range(int(input())):
    n=int(input())
    def chk(n):
        if n%2==0:
            while n%2==0:
                n=n/2
                if n==1:
                    return "NO"
                if n%2!=0:
                   return("Yes")

        else:
           return "YES"
    print(chk(n))