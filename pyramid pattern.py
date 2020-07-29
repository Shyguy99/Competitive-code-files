n=int(input())

for i in range(1,n+1):

        for k in range(1,n-i+1):
            print(" ",end=" ")
        for a in range(1,((i*2))):
            if a%2==1:
                print("#",end=" ")
            if a%2==0:
                print(" ",end=" ")
        for z in range(1,n-i+1):
            print(" ",end=" ")
        print("\n")
