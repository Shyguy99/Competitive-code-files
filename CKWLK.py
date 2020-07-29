import math
for _ in range(int(input())):
    n=int(input())
    aa=list(str(n))
    f1=str(n)
    f2=[]
    j=len(aa)-1
    while j!=0:
        if aa[j]=='0':
            f2.append('0')
            f1=f1[:-1]
        else:
            break
        j-=1
    s=math.log(int(f1),2)

    if s-int(s)==0.0:
        if int(s) <= f2.count('0'):
            print("Yes")
        else:
            print("No")
    else:
        print("No")