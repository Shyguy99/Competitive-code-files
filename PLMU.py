from math import factorial as ft
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    c0=a.count(0)
    c1=a.count(1)
    c2=a.count(2)
    su=0
    if c0>1:
        su=su+(ft(c0)/(ft(c0-2)*ft(2)))
    if c1>1:
        su=su+(ft(c1)/(ft(c1-2)*ft(2)))
    if c2>1:
        su=su+(ft(c2)/(ft(c2-2)*ft(2)))
    print(int(su))