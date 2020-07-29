ll,r=list(map(int,input().split()))
def check(x):
    e = 0
    o = 0
    for m in str(x):
        if int(m) % 2 == 0:
            e += 1
        else:
            o += 1
    if e % 2 != 0 and o % 2 == 0:return 1
    else:return 0
def ccount(l):
    s=str(l)
    s=len(s)-1
    if s%2==0:
        s=s-1
    ten=1
    co=0
    for i in range(1,s+1,2):
        co=co+(5*ten)
        ten=pow(10,i)*9
    k="9"*(len(str(l))-1)
    if k=="":
        k=0
    if len(str(l))%2!=0:
       left_nums=l-int(k)
       print(left_nums)
       dleft_nums=left_nums//10
       print(dleft_nums)
       leftco=dleft_nums*5
       co=co+leftco
       global finleft

       finleft=left_nums-dleft_nums*10
       print(finleft)
       print(co)
       for j in range(l-finleft+1,l):
             print(j)
             co +=check(j)
    return co


a=ccount(ll)
b=ccount(r)
q=0
if finleft>0:
    q=check(r)
print(b-a+q)

