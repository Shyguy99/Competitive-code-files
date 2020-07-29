for _ in range(int(input())):
    n=int(input())
    c=list(map(int,input().split()))
    x=int(input())
    sss=0
    m=0
    l=n-1
    oo=0
    pp=0
    while(sss==0):
            c[m]=c[m]-x-oo
            oo=0
            if c[m]<=0:
                oo=c[m]
                m+=1
            c[l]=c[l]-1-pp
            pp=0
            if c[l]<=0:
                pp=c[l]
                l-=1
            if m==l:

                if m+1>=n-(m+2):
                    fi1=m+1
                    fi2=n-(m+1)
                    break
                elif m+1<n-(m+2):
                    fi1=m
                    fi2=n-(m)
                    break
    print(fi1,fi2)

