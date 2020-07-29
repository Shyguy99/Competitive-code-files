for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    ll=0
    if a[0] >= a[-1]:
        fi=a[0]
        a.remove(a[0])
    else:
        fi=a[-1]
        a.remove(a[-1])
    co=fi
    for i in range(n-1):
        if a[0]>=a[-1]:
            fi=a[0]
            a.remove(a[0])
        else:
            fi=a[-1]
            a.remove(a[-1])
        if fi>co:
            ll=1
            break
        co=fi
    if ll==1:
        print("No")
    else:
        print("Yes")