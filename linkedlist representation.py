class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def prin(self):
        temp=self.head
        while(temp):
            print(temp.data,end=" ")
            temp=temp.next

    def reverloop(self):
        st=self.head
        o=None

        while st:
            ne=st.next
            st.next=o
            o=st
            if ne==None:
                break
            st=ne
        self.head=st
    def reverp(self,s):
         if s:
            self.reverp(s.next)
            print(s.data,end=" ")
         else:
            return



li=list(map(int,input().split()))
lk=LinkedList()
lk.head=Node(li[0])
g=lk.head
for i in range(1,len(li)):
    g.next=Node(li[i])
    g=g.next


lk.prin()
print()
#lk.reverp(lk.head)
#lk.reverloop()
print()
lk.prin()
