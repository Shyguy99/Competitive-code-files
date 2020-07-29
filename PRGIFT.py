for _ in range(int(input())):
    n,k=list(map(int,input().split()))
    a=list(map(int,input().split()))
    c=0
    chk=0
    for i in range(n):
        if a[i]%2==0:
            c+=1
    if c==n and k==0:
            print("NO")

    elif c>=k:
        print("YES")
    else:
        print("NO")
