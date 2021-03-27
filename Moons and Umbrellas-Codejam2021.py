for _ in range(1,int(input())+1):
    x,y,s=map(str,input().split())
    x=int(x)
    y=int(y)
    n=len(s)
    s=list(s)

    def fun(x,y,s):
        st=-1
        en=-1
        temp=[]
        fin=0
        for i in range(n):
            if st==-1:
               temp.append(s[i])
               st=1
            elif st!=-1:
                if s[i]=='?' and i!=n-1:
                    temp.append('?')
                else:
                   en=1
                   temp.append(s[i])
                   st=0

                   if temp[0]=='?' or temp[-1]=='?':
                       pass
                   else:
                     if temp[0]+temp[-1]=="CJ":
                          fin+=x
                     elif temp[0]+temp[-1]=="JC":
                          fin+=y
                   temp=[temp[-1]]


        print("Case #{}: {}".format(_, fin))


    fun(x, y, s)





