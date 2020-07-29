import math
s=input()
s.replace(" ","")
n=len(s)
l=math.floor(math.sqrt(n))
u=math.ceil(math.sqrt(n))
if l*u<n:
    l=l+1
k=""
for i in range(u):
    a=""
    d = i
    for j in range(l):
        try:
           a=a+s[d]
           d=d+u
        except IndexError:
            break
    k=k+a+" "
print(k)