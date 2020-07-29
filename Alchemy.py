for _ in range(1,int(input())+1):
    n=int(input())
    s=list(input())
    a=s.count("A")
    b=s.count("B")
    if abs(a-b)==1:
        print("Case #{}:{}".format(_,"Y"))
    else:
        print("Case #{}:{}".format(_,"N"))
