for _  in range(int(input())):
    s=list(input())

    a=['p','a','r','t','y']
    b = ['p', 'a', 'w', 'r', 'i']
    for i in range(len(s)-3):
        if s[i:i+5]==a:
            for k in range(5):
                s[i+k]=b[k]
    l=""
    l=l.join(s)
    print(l)

