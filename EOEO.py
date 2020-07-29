for _ in range(int(input())):
    n=int(input())
    if n%2!=0:
       pass
    else:
        while n%2==0:
            n=n//2
    k=int(n//2)
    print(k)