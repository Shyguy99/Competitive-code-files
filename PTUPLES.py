

def prime_n(n):
    global a

    prim = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):
        if (prim[p] == True):

            # Update all multiples of p
            for i in range(p * 2, n + 1, p):
                prim[i] = False
        p += 1
    prim[0] = False
    prim[1] = False
    for p in range(n + 1):
        if prim[p]:
            a.append(p)


a = []
prime_n(1000000)
fi=[0]
k=0
for i in range(len(a)-1):
    if a[i+1]-a[i]==2:
        k+=1
        fi.append(k)

    else:
       fi.append(k)

for _ in range(int(input())):
    n=int(input())

    def search(f):
        ans=0
        i=0
        j=len(a)-1
        while i<=j:
            mid = (i + j) // 2

            if a[mid]==f:
                return mid
            elif a[mid]<f:
                ans=mid
                i=mid+1
            else:
                j=mid-1
        return ans

    ff=search(n)
    print(fi[ff])