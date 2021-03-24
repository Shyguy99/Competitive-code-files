for _ in range(int(input())):
    w1,w2,x1,x2,m=map(int,input().split())

    a=m*x1+(w1)
    b=m*x2+(w1)
    if a<=w2<=b:
        print(1)
    else:
        print(0)
