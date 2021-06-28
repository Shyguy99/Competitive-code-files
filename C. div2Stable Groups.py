n,k,x=map(int,input().split())

a=list(map(int,input().split()))
a.sort()
count=0
print(a)
i=0
diff=[]
while i<n-1:
    if a[i+1]-a[i]<=x:
        i+=1
        continue
    else:
            diff.append(a[i+1]-a[i]-1)
            count+=1
            print(a[i])
            i+=1
count+=1
print(diff)
print(count)

diff.sort()
for i in range(len(diff)):
    l=diff[i]//x
    if k-l>=0:
        count-=1
        k=k-l
print(count)
