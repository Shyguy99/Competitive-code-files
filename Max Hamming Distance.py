from collections import defaultdict
s=input()
a=defaultdict()
for i in s:
    if i in a:
       a[i]+=1
    else:
       a[i]=1
to=len(s)
p=to
for j in a:
    q=a[j]
    if to-q<q:
        p-=(q-to+q)
print(p)
