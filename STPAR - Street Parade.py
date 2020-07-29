while True:
    n=int(input())
    if n==0:
        break
    a=list(map(int,input().split()))
    s1=a[::-1]
    s2=[]
    s3=[]
    flag=0
    while len(s1)>0:
       if len(s3) and len(s2)!=0 and s2[-1]<s3[-1]<s1[-1]:
               s2.append(s3.pop())
       elif s1[-1]!=min(s1):
           s3.append(s1.pop())
           if s3[-1]!=min(s3):
               flag=1
               break
       else:
           s2.append(s1.pop())
    if flag!=1:
        while len(s3)>0:
           s2.append(s3.pop())
    a.sort()
    if a!=s2 or flag==1:
        print("no")
    else:
        print("yes")
