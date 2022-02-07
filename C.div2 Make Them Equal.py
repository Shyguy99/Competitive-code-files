for _ in range(int(input())):

    n,x=map(str,input().split())
    s=input()
    n=int(n)
    if s.count(x)==n:
        print(0)
    elif s[n-1]==x:
        print(1)
        print(n)
    else:
        i=n-1
        flag=0
        while i>=n//2:

            if s[i]==x:
                flag=1
                break
            i-=1
        if flag==1:
            print(1)
            print(i)
        else:
            print(2)
            print(n,n-1)

