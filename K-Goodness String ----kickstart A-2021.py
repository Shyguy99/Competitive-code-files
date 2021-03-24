for z in range(1,int(input())+1):
    n, k = map(int, input().split())
    s = input()

    i = 0
    j = n - 1
    f = 0
    while i < j:
        if s[i] != s[j]:
            f += 1
        i += 1
        j -= 1
    if f == k:
        print("Case #{}: {}".format(z, 0))
    else:
        print("Case #{}: {}".format(z, abs(k - f)))