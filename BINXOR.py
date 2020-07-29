for _ in range(int(input())):
    n=int(input())
    a1=input()
    a2=input()
    def btoi(C):
       binary =int(C)
       decimal, i, n = 0, 0, 0
       while (binary != 0):
           dec = binary % 10
           decimal = decimal + dec * pow(2, i)
           binary = binary // 10
           i += 1
       return(decimal)
