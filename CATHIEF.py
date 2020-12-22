for i  in range(int(input())):
    x,y,k,n=list(map(int,input().split()))
    if abs(x-y)%2==0:
        a=abs(x-y)/2
        if a%k==0:
            print("Yes")
        else:
            print("No")
    else:
      print("No")