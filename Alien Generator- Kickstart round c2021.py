import math
for _ in range(1,int(input())+1):
    g=int(input())

    x=1
    co=0
    while x<=int(math.sqrt(g))*2:
        l=(g-(x*(x-1)/2))/(x)
        if int(l)==l:
            co+=1
        x+=1
    print("Case #{}: {}".format(_, co))
