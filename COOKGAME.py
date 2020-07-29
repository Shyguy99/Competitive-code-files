for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    def ans(n,a):
        if a[0]!=-1 and a[0]!=1:
            return 0
        else:
            a[0]=1
        if a[n-1]==-1:
            a.insert(1,n)
            n=n+1
        cout=0
        k=1
        fin=1
        for i in range(n):
            if a[i]==-1:
                   cout+=1
            elif a[i]>=1:
               if cout>0:
                   to=pow(2,cout)
                   if a[i]==k+cout+1:
                       tu=1
                   else:
                       tu=to/(pow(2,(a[i]-1)))
                   fin=(fin*int(tu))
                   cout=0
               k=a[i]
            else:
                   return 0
        return fin
    print(ans(n,a)%(10**9+7))


#wrong