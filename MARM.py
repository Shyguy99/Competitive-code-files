for _ in range(int(input())):
    n,k=list(map(int,input().split()))
    A=list(map(int,input().split()))
    for i in range(k):
        a=A[i%n]
        b=A[n-(i%n)-1]
        A[i % n]=a^b
        print(A)
    print(*A)