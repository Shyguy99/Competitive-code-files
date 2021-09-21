import math

for _ in range(int(input())):
    x,l,r=map(int,input().split())

    num_x=int(math.log2(x))
    num_r=int(math.log2(r))

    bin_s='0'*(max(num_r-num_x,0))+"{0:b}".format(x)

    k=0
    fin=''
    n=len(bin_s)
    for i in range(n):
        if bin_s[i]=='0':
            temp=2**(n-i-1)
            if k+temp>r:
                fin+='0'
            else:
               k+=temp
               fin+='1'
        else:
           z=0
           y=n-i-2
           while y>=0:
               z+=2**y
               y-=1
           if k+z<l:
                fin+='1'
                k+=2**(n-i-1)
           else:
               fin+='0'
    fin=int(fin,2)
    print(x^fin)



