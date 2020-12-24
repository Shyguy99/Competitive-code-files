n=int(input())
a=list(map(int,input().split()))
a.sort()
k=[]
j=0
for i in a:
    if j<=i:
        k.append(i)
        j+=i
print(len(k))