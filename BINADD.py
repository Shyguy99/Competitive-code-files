for _ in range(int(input())):
    AA=input()
    BB=input()
    def btoi(C):
       binary =int(C)
       decimal, i, n = 0, 0, 0
       while (binary != 0):
           dec = binary % 10
           decimal = decimal + dec * pow(2, i)
           binary = binary // 10
           i += 1
       return(decimal)
    A=btoi(AA)
    B=btoi(BB)
    cout=0
    while B>0:
        U = A^B
        V = A & B
        A = U
        B = V * 2
        cout+=1
    print(cout)

#partial