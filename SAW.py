n=int(input())
a=[]
for i in range(1,n+1):
    a.append(i)
while len(a)!=1:
    p=len(a)
    s=a[:]
    for k in range(1,len(a)+1):
        if k%2==0:
            s.remove(a[k-1])
    if p%2!=0:
        s.remove(a[0])
    a=s[:]
print(a[0])


