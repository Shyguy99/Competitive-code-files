for z in range(1,int(input())+1):
    n=int(input())
    a=list(map(int,input().split()))

    p=0
    k=1
    i=0
    fin=0
    while i <n:

        if a[i]==k:
            s=a[p:i+1]
            s=s[::-1]
            fin+=len(s)
            a=a[0:p]+s+a[i+1:]
            p+=1
            k+=1
            i=k-2


        i+=1
    print("Case #{}: {}".format(z,fin-1))