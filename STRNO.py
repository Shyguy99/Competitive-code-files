#wrong

for _ in range(int(input())):
    x,k=list(map(int,input().split()))
    p=2
    q=0
    l=2
    mul=1
    def pp(n):
        if (n <= 1):
            return False
        if (n <= 3):
            return True

        if (n % 2 == 0 or n % 3 == 0):
            return False
        i = 5
        while (i * i <= n):
            if (n % i == 0 or n % (i + 2) == 0):
                return False
            i = i + 6

        return True

    while (p!=(x-k) or q!=k):
       if pp(l) and q!=k:
           print("p== ",l,p,q)
           q+=1
           mul*=l
       elif not pp(l) and p<(x-k):
           print(l,p,q)
           p+=1
           mul*=l
       l+=1
    print(mul)