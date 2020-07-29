n,q=list(map(int,input().split()))
a=list(map(int,input().split()))
for i in range(q):
    l,r=list(map(int,input().split()))
    ic=0
    dc=0
    if a[l]>a[l-1]:
            ic+=1
            k=1
    else:
            dc+=1
            k=-1
    for j in range(l+1,r):
        b= a[j]-a[j-1]
        if b>0:
            oo=1
        else:
            oo=-1
            
        if oo!=k:
            if oo==1:
                ic+=1
            else:
                dc+=1
        k=oo
       
    if ic==dc:
        print("YES")
    else:
        print("NO")
            
            
            
         
        
    