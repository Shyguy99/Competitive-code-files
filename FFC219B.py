from math import factorial
for _ in range(int(input())):
    l,r=list(map(int,input().split()))
    su=0
    for i in range(l,r+1):
        su=(su+(i*(i+1)*(i+2)*(i+3)))%1000000007
    print(su)