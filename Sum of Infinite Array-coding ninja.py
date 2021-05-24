
def sumInRanges(arr, n, queries, q):

    for i in range(1 ,n):
        arr[i ] =arr[i ] +arr[ i -1]
    fin =[]
    for i in range(q):
        l=queries[ i][0]-1
        r=queries [ i][1]-1

        p1=(l)//n
        if ((l ) %n)-1==-1:
            k=0
        else:
            k=arr[((l ) %n)-1]
        s1=p1*arr[ - 1] + k

        p2=(r+1)// n
        if ((r+1) %n)-1==-1:
            k=0
        else:
            k=arr[((r+1 ) %n)-1]
        s2=p2*arr[ - 1] + k

        fin.append (s2-s1)
    return(fin)

for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    q=int(input())
    que=[]
    for i in range(q):
        l,r=map(int,input().split())
        que.append([l,r])
    print(*sumInRanges(arr,n,que,q))

