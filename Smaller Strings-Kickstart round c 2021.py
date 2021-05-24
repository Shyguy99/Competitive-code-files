for _ in range(1,int(input())+1):
       n,k=map(int,input().split())
       s=input()
       n=len(s)
       mod=(10**9)+7

       if n%2==0:
           l=s[:(n//2)]
           t = l[:]
           temp = l + t[::-1]

       else:
           l=s[:(n//2)+1]
           t=l[:len(l)-1]
           temp=l+t[::-1]

       co=0
       if temp<s and temp!=s:
           co+=1
       ss=pow(k,len(l)-1)
       tt=1
       for i in range(len(l)):
          p=ord(l[i])-96
          co=co+((p-1)*ss//tt)%mod
          tt*=k

       print("Case #{}: {}".format(_,co))



