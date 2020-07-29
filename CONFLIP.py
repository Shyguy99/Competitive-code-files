for _ in range(int(input())):
    for __ in range(int(input())):
        i,n,q=list(map(int,input().split()))
        if n%2==0:
            print(int(n/2))
        else:
            if i==q:
                print(n//2)
            else:
                print((n//2)+1)

