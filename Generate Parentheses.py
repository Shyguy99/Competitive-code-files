n=int(input())
i=0
s=""
res=[]
j=0
def done(s,n,i,j,res):
    if i<n:
        done(s+"(",n,i+1,j,res)
    if j<i:
        done(s+")",n,i,j+1,res)
    else:
        if len(s)==n*2:
          res.append(s)
done(s,n,i,j,res)
print(res)


