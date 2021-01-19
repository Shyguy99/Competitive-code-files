# code
for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    neg = 0
    pos = 0
    all_pos = []
    for i in range(n):
        if a[i] >= 0:
            pos += 1
            all_pos.append(a[i])
        else:
            neg += 1
            all_pos.append(abs(a[i]))
    if k == neg:
        print(sum(all_pos))
        continue
    elif k > neg:
        if k - neg & 1:
            print(sum(all_pos) - min(all_pos))
            continue
        else:
            print(sum(all_pos))
            continue
    else:
        a.sort()
        print(sum(abs(a[j]) for j in range(k)) + sum(a[neg:])+sum(a[k:neg]))


