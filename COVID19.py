for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    m=[]
    for i in range(n):
        l=1
        for j in range(i,0,-1):
            if a[j]-a[j-1]<=2:
                l+=1
            else:
                break
        for k in range(i,n-1):
            if a[k+1]-a[k]<=2:
                l+=1
            else:
                break
        m.append(l)
    print(min(m),max(m))




