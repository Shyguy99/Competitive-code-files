for _ in range(int(input())):
    n, k = map(int, input().split())

    s = input()
    s = list(s)

    if s.count('*') <= 2:
        print(s.count('*'))
    else:
        i = 0
        f1 = 0
        t = 0
        count = 0
        bre2=0
        while i < n:
            print(s)
            if s[i] == '*' and f1 == 0:
                f1=1
                count += 1
                s[i] = 'x'
                t=0
            else:
                t += 1
            j = i

            if t >= k and f1==1:
                while j >= 0:
                    if s[j]=='x':
                        bre2=1
                        break

                    if s[j] == '*':
                        s[j] = 'x'
                        count+=1
                        break
                    j-=1
                t=0
                if bre2==1:
                    break
            i=j+1
        j=n-1
        while j>=0:
            if s[j]=='x':
                 break
            if s[j]=='*':
                count+=1
                s[j]='x'
                break
            j-=1
        print(count)
