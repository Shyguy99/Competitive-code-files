n=int(input())
a=list(map(int,input().split()))
s=[]
su=0
for i in a:
    su=su+i
    s.append(su)
m=int(input())
for j in range(m):
    t=int(input())
    if t>s[-1]:
        print(-1)
    else:
       for k in range(len(s)):
         if s[k]>=t:
             print(k+1)
             break