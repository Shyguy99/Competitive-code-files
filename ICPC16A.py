for _ in range(int(input())):
    x1,y1,x2,y2=list(map(int,input().split()))
    if x1>x2 and y1==y2:
        print("left")
    elif x1<x2 and y1 == y2:
            print("right")
    elif x1==x2 and y1>y2:
        print("down")
    elif x1==x2 and y1<y2:
        print("up")
    else:
        print("sad")
