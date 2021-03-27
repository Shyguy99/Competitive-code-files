for _ in range(int(input())):
    a,y,x=map(int,input().split())
    li=[]


    k=a
    fin=a+1
    if k-y>=0:
        fin-=(1+k-y)
        ans=fin*x
    else:
        ans=1+(a*x)

    print(ans)