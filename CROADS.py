from math import log2
for _ in range(int(input())):
    n=int(input())
    if int(log2(n))==log2(n):
        print(-1)
    else:
        print(n/2)