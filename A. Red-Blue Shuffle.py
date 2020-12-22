for i in range(int(input())):
    n=int(input())
    c1=list(input())
    c2=list(input())
    p1=0
    p2=0
    for j in range(n-1,-1,-1):
        if c1[j]>c2[j]:
            p1+=1
        elif c1[j]<c2[j]:
            p2+=1
    if p1>p2:
        print("RED")
    elif p1<p2:
        print("BLUE")
    else:
        print("EQUAL")


