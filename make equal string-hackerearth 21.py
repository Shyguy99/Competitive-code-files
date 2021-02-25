from collections import defaultdict
from collections import Counter
for _ in range(int(input())):
    n=int(input())
    s=list(input())
    t=list(input())
    s_con=Counter(s)
    t_con=Counter(t)
    def count_same(s_con,t_con):
        p=False
        for i in s_con:
            if s_con[i]>1:
                p=True
            if not s_con[i]==t_con[i]:
                return p,False
        return p,True


    def CountSteps(s1, s2, size):

        i = 0
        j = 0
        result =0
        while (i < size):
            j = i
            while (s1[j] != s2[i]):
                j += 1
            while (i < j):

                temp = s1[j]
                s1[j] = s1[j - 1]
                s1[j - 1] = temp
                j -= 1
                result += 1

            i += 1

        return result
    def can_con(s,t,n,s_con,t_con):
        m_one,is_same= count_same(s_con,t_con)
        if is_same:

            if m_one:
                return "YES"


            #s_dict=defaultdict(list)
            #t_dict=defaultdict(list)
            #for i in range(n):
                #s_dict[s[i]]=i
            r=CountSteps(s,t,n)
            if r%2==0:
                return "YES"
            else:
                return "NO"
        else:
            return "NO"

    print(can_con(s,t,n,s_con,t_con))