for _ in range(int(input())):
    s,sg,fg,d,t=list(map(int,input().split()))
    k=((d*50*3.6)/t)+s
    if abs(k-sg) >abs(k-fg):
        print("FATHER")
    elif abs(k-sg)<abs(k-fg):
        print("SEBI")
    else:
        print("DRAW")
