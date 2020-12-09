def f():
    c=0
    n=int(input())
    if n==1:
        return 0
    while True:
        if n == 2:
            c += 1
            return c
        if n%2!=0:
            n=n-1
            c+=1
        else:
           n=2
           c+=1
for z in range(int(input())):
    print(f())

