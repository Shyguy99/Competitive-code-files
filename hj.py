p=int(input())
q=int(input())
r=int(input())
s=int(input())
fin=0
for l in range(p,q+1):
    for j in range(r,s+1):
        a,b=l,j
        i=max(a,b)-min(a,b)
        k=1
        while i !=0:
            if a>b:
                    a=i
            else:
                    b=i
            i=max(a,b)-min(a,b)
            k+=1
        fin+=k
print(fin)