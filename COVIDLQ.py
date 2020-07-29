t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    j=0
    c=0
    a=[]
    while j<n:
        if l[j]==1:
            c+=1
            d=j
            a.append(d)
        j=j+1
    if c==1:
        print("YES")
    if c>1:
        v=0
        for k in range(1,len(a)):
          if a[k]-a[k-1]>=6:
              v+=1
        if v==len(a)-1:
            print("YES")
        else:
            print("NO")