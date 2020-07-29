from math import factorial
n,k=list(map(int,input().split()))
a=list(map(int,input().split()))
summ=1
for r in range(1,k+1):
    l=factorial(n) / (factorial(r) * factorial(n-r))
    summ=(summ+l)%1000000007
print(int(summ))
