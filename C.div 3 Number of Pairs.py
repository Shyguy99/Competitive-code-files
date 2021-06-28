import time
def smaller(i,j,k):

    ans=-1
    while i<=j:

        mid=(i+j)//2

        if a[mid]<=k:
             ans=mid
             i=mid+1
        else:
            j=mid-1
    return ans


def greater(i,j, k):

    ans = -1
    while i <= j:

        mid = (i + j) // 2

        if a[mid] <k:
            i = mid + 1
        else:
            ans = mid
            j = mid - 1
    return ans
for _ in range(int(input())):
    tim=time.time()
    n,l,r=map(int,input().split())
    a=list(map(int,input().split()))

    a.sort()

    fin=0
    for i in range(n):

        gr=l-a[i]
        sm=r-a[i]

        get_gr=greater(i+1,n-1,gr)
        if get_gr==-1:
            continue

        get_sm=smaller(i+1,n-1,sm)
        if get_sm==-1:
            continue
        fin+=get_sm-get_gr+1
    tim2=time.time()
    print(fin)


