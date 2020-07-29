n=int(input())
k=int(input())
se=['a','b','c']
i=1
s=" "
fin=[]
def done(i,s):
   if i<=n:
    for l in se:
        if s[-1]!=l:
            done(i+1,s+l)
   if len(s)==n+1:
     fin.append(s[1:])
done(i,s)
fin.sort()
if len(fin)<k:
    print("")
else:
    print(fin[k-1])
