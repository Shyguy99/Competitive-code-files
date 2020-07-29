n,m=list(map(int,input().split()))
nl=(list(map(int,input().split())))
a=set(list(map(int,input().split())))
b=set(list(map(int,input().split())))
c=0
for i in nl:
   if i in a:
       c+=1
   if i in b:
       c-=1
print(c)