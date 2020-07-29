n=int(input())
def done(aa,res,l,n):
     global fin
     for j in aa:
         if j not in res and (j%l==0 or l%j==0):
             done(aa,res+[j],l+1,n)
     if len(res)==n:
                fin+=1

fin=0
l=1
aa=list(a for a in range(1,n+1))
res=[]
done(aa,res,l,n)
print(fin)
