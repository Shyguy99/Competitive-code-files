for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))



    def solve(a,n):
        di=dict()
        for i in a:
            di[i]=1
        fin=100000
        for j in range(1,n):
            k=a[0]^a[j]
            di_t=dict()
            c=0
            s=[]
            for i in range(n):
                s.append(a[i]^k)

                if a[i]^k in di and a[i]^k not in di_t:
                    di_t[a[i]^k]=1
                    c+=1
            if c==n:
                fin=min(fin,k)
        return fin if fin!=100000 else -1
    print(solve(a,n))