
# s=list(input())
# fi=0
# q=0
# w=0
# def t(i):
#     try:
#         int(s[i+1])
#         return int(s[i+1])
#     except ValueError:
#         return 1
#     except IndexError:
#         return 1
# a=[]
#
# for i in range(len(s)):
#     f=s[i]
#     if f=='(':
#         a.append(f)
#         q=q+w
#         w=0
#         print(a)
#         print(q,w,"(((((((((((((((")
#     elif f=='C':
#         if len(a)==0:
#             q=q+12*t(i)
#         else:
#             w=w+12*t(i)
#         print(w,"w")
#     elif f=='H':
#         if len(a)==0:
#             q=q+1*t(i)
#         else:
#             w=w+1*t(i)
#         print(w,"w")
#     elif f=='O':
#         if len(a)==0:
#             q=q+16*t(i)
#         else:
#             w=w+16*t(i)
#         print(w,"w")
#
#     if f==')' or i==len(s)-1:
#         if len(a)>0:
#           a.pop()
#         q=q+w
#         w=0
#         print(a, f,q,"-q",w,"-w")
#     if len(a)==0 :
#         print(a)
#         fi=fi+q*t(i)
#         q=0
#         print(q,"-q",fi,"fiiiiiiiiiiii")
#
# print(fi)
#

#WRONG
