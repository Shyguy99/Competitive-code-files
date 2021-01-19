for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    def f(a):
        one=a.count(1)
        if one==0:
            if a.count(2)%2!=0:
                return ("NO")
            else:
                return("YES")
        elif one%2!=0:
            return("NO")
        else:
            return("YES")
    print(f(a))