
def bcount(s):
    sl = s + s
    c = 0
    max = 0
    for i in range(len(s)-1,-1,-1):
         if s[i]=='0':
            c+=1
         else:
            break
         if c==len(s):
            return -1
    max=c
    for j in range(len(s),len(sl)):
         if sl[j]=='0':
             c+=1
         else:
             c=0
         if max<c and c!=len(s):
             max=c
         elif c==len(s):
             return -1
    return max
s = input()
print(bcount(s))

