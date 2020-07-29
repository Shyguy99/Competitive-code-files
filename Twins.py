from math import sqrt
import time
m,n=list(map(int,input().split()))
def pri(o):
    if o==1:
        return False
    elif o==2:
        return True
    if o>2 and o%2==0:
        return False
    else:
        oo = int(sqrt(o))
        for l in range(3,oo+1,2):
            if o%l==0:
                return False
        return True
q=[]
t1=time.time()
for o in range(m,n+1):
    if pri(o):
        q.append(o)
t2=time.time()
print(t2-t1)
print(len(q))
cou = 0
l = 0
r = 0
while r <len(q):
    if q[r] - q[l] == 2:
        cou += 1
        l += 1
        r += 1

    # arr[r] - arr[l] < sum
    elif q[r] - q[l] > 2:
        l += 1
    else:
        r += 1
print(cou)
