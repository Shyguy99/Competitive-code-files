for _ in range(int(input())):
    m,n=list(map(int,input().split()))
    a=min(m,n)
    for i in range(1,a+1):
        if m%i==0 and n%i==0:
            hcf=i
    lcm=int(m*n/hcf)
    print(hcf,lcm)