n=int(input())
dh=list(map(int,input().split()))
nob=int(input())
db=list(map(int,input().split()))
cout=[]
fi=[]
for l in range(1,n+1):
    cout.append(l)
for i in range(nob):
    o=0
    j=n-1
    while j>=0:
        if db[i]<=dh[j]:
            cout[j]-=1
            if cout[j]>=0:
                fi.append(j+1)
                break
            else:
                o+=1
        else:
            o+=1
        j-=1
    if o==len(dh):
        fi.append(0)
print(*fi)
