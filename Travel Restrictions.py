for _ in range(1,int(input())+1):
    n=int(input())
    incom=input()
    outcom=input()
    i=0
    print("Case #{}:".format(_))

    while i<n:
       j=i
       k=i+1
       s1=""
       while j>=0:
           if j==i:
               s1=s1+'Y'
               j-=1
           else:
               if incom[j]=='Y' and outcom[j+1]=="Y":
                   s1+="Y"
                   j-=1
               else:
                   s1+="N"
                   j-=1
                   break

       while j>=0:
           s1+="N"
           j-=1
       s1=s1[::-1]
       s2=""
       while k<=n-1:
           if incom[k]=="Y" and outcom[k-1]=="Y":
               s2+="Y"
               k+=1
           else:
               s2+="N"
               k+=1
               break
       while k<=n-1:
           s2+="N"
           k+=1

       i+=1

       fins=s1+s2
       print(fins)



