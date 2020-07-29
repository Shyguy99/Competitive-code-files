summ1=summ2=l1=l2=0
for _ in range(int(input())):
    p1,p2=list(map(int,input().split()))
    summ1+=p1
    summ2+=p2
    dif=summ1-summ2
    if dif<=0:
        if abs(dif)>l2:
          l2=abs(dif)
    else:
        if abs(dif) > l1:
           l1=abs(dif)
if l1<=l2:
    print(2,l2)
else:
    print(1,l1)

