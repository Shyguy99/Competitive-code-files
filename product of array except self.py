a1=1
a2=1
af=[1]
ab=[1]
fin=[]
num=[1,2,3,4]
n=len(num)
for i in range(1,n):
    a1=a1*num[i-1]
    af.append(a1)
j=n-2
while j>=0:
    a2=a2*num[j+1]
    ab.append(a2)
    j-=1
ab=ab[::-1]
for k in range(n):
    fin.append(af[k]*ab[k])
print(fin)