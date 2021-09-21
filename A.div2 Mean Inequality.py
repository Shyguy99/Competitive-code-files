for _ in range(int(input())):
    a = list(map(int, input().split()))

    m1 = 0
    m2 = 0
    in1 = 0
    in2 = 0
    for i in range(len(a)):
        if m1 < a[i]:
            m2=m1
            in2=in1
            m1 = a[i]
            in1 = i
        elif a[i] > m2:
            m2 = a[i]
            in2 = i
    if abs(in1 - in2) > 1:
        print("YES")
    elif (in1 % 2 == 0 and in2 != in1 + 1) or (in2 % 2 == 0 and in1 != in2 + 1):
        print("YES")
    else:
        print("NO")
