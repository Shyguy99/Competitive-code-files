for _ in range(int(input())):
    n=int(input())
    li=list(map(int,input().split()))

    def chk(li,n):
        li.sort(reverse=True)
        i=0
        while i<2*n-1:
            if li[i]%2!=0:
                return "NO"
            if li[i]==li[i+1] and (i==2*n-2 or li[i]!=li[i+2]):
                pass
            else:
                return"NO"
            i+=2
        fin=[]
        te=0
        p=2*n
        for k in range(0,2*n-1,2):
            if (li[k]-te)%p==0 and li[k]-te>0 :
                ad=int((li[k]-te)/p)
                fin.append(ad)
                p-=2
                te+=2*ad
            else:
               return "NO"


        return "YES"
    print(chk(li,n))


