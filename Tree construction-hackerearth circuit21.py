import math
from _collections import defaultdict

class Node:
    def __init__(self,a):
        self.val=a
        self.left=None
        self.right=None
n,m=map(int,input().split())

root=Node(1)
i=2
j=0
qu=[root]
ga=defaultdict(list)
parent=defaultdict()
while i<n+1:
    a=qu[j]
    j+=1
    a.left=Node(i)
    ga[a.val].append(i)
    parent[i]=a.val
    qu.append(a.left)
    i+=1
    if i==n+1:
        break
    a.right=Node(i)
    ga[a.val].append(i)
    parent[i]=a.val
    qu.append(a.right)
    i+=1
def sum_sub(root):
    global summ
    if root.left!=None and root.right!=None:
        r=1+sum_sub(root.left)+sum_sub(root.right)
        summ+=r
        return r
    elif root.left==None and root.right==None:
        summ+=1
        return 1

    elif root.left!=None:

        r= 1+sum_sub(root.left)
        summ+=r
        return r
    else:
        r=1+sum_sub(root.right)
        summ+=r
        return r
def all_left_node(root,lef):
    if root==None:
        return lef
    else:
        lef.append(root.val)
        return  all_left_node(root.left,lef)

summ=0
sum_sub(root)
minn=summ
maxx=int(n*(n+1)/2)
lvl=1+math.floor(math.log2(n))
print(lvl)
print(ga)
print(minn,maxx)

left_nodes=all_left_node(root,[])
print(left_nodes)

#making the required tree if possible
if m>=minn and m<=maxx:
    s=minn
    all_nodes=[i for i in range(1,n+1)]
    print(all_nodes)
    while s!=m:
        print(s)
        k=all_nodes.pop()
        if k not in left_nodes:
            lvl_k=1+math.floor(math.log2(k))
            r=len(left_nodes)-lvl_k+1
            if s+r<=m:
                s+=r
                ga[left_nodes[-1]].append(k)
                ga[parent[k]].remove(k)
                left_nodes.append(k)
            else:
                extra_s=s+r-m
                l=-1-extra_s
                s=m
                ga[left_nodes[l]].append(k)
                ga[parent[k]].remove(k)
                left_nodes.append(k)
    for ver, con in ga.items():
        for l in con:
            print(ver, l)
else:
    print(-1)





