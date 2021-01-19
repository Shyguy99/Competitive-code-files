for _ in range(int(input())):
    a,b,n=map(int,input().split())

    def f(a,b,n):
       c=1
       while a%2==0:
            c*=2
            a=a/2
            if c>=n:
                return("YES")
       while b%2==0:
           c*=2
           b=b/2
           if c>=n:
               return("YES")
       if c>=n:
           return ("YES")
       else:
           return("NO")
    print(f(a,b,n))