from collections import defaultdict

for i in range(int(input())):
    a,b,k=map(int,input().split())
    ar=list(map(int,input().split()))
    br=list(map(int,input().split()))
    ga=defaultdict(list)
    for i in range(k):
        ga[ar[i]].append(-1*br[i])
        ga[-1*br[i]].append(ar[i])
    c=0
    print(ga)
    for i in range(k):
       a1=ar[i]
       b1=-1*br[i]
       c+=k-1-(len(ga[a1])-1)-(len(ga[b1])-1)
    print(int(c/2))