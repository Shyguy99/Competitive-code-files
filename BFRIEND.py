for _ in range(int(input())):
    n,a,b,c=list(map(int,input().split()))
    f=list(map(int,input().split()))
    m=1000000000000
    if a<b:
       for i in range(len(f)):
           if f[i]<b and f[i]>a:
               k=abs(a-b)
               break
           elif f[i]>b:
               k=(f[i]-b)+(f[i]-a)
           else:
               k=(a-f[i])+(b-f[i])
           if k<m:
               m=k   
    else:
        for i in range(len(f)):
           if f[i]<a and f[i]>b:
               k=0
               break
           elif f[i]<b:
                k=(b-f[i])+(a-f[i])
           else:
               k=(f[i]-a)+(f[i]-b)
           if k<m:
               m=k
               
    print(m+c)