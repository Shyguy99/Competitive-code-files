for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    rem0=0
    rem1=0
    rem2=0
    for i in a:
        if i%3==0:
            rem0+=1
        elif i%3==1:
            rem1+=1
        else:
            rem2+=1
    if rem0==1:
        print("Yes")
    elif rem0>1 and rem0<=(rem1+rem2+1):
        print("Yes")
    else:
        print("No")
