import sys


def cons(arr,st,l,r,pos):

    if l==r:
        st[pos]=arr[l]
        return arr[l]

    mid=(l+r)//2

    st[pos]=min(cons(arr,st,l,mid,2*pos+1),cons(arr,st,mid+1,r,2*pos+2))
    return st[pos]


def query(st,l,r,s,e,pos):
    if l>=s and r<=e:
        return st[pos]

    if r<s or e<l:
        return sys.maxsize

    else:
        mid=(l+r)//2
        return min(query(st,l,mid,s,e,2*pos+1),query(st,mid+1,r,s,e,2*pos+2))


def update(st,l,r,i,d,pos):

    if i<l or i>r:
        return st[pos]
    if i==r and  i==l:
        return d
    mid=(l+r)//2
    st[pos]=min(update(st,l,mid,i,d,2*pos+1),update(st,mid+1,r,i,d,2*pos+2))
    return st[pos]


arr=list(map(int,input().split()))
n=len(arr)

st=[sys.maxsize for i in range(2*n-1)]
l=0
r=n-1
pos=0
cons(arr,st,l,r,pos)
print(st)

q=int(input())
for i in range(q):
    qry,a,b=map(int,input().split())
    if qry==1:

        print(query(st,0,n-1,a-1,b-1,0))
    else:
        update(st,0,n-1,a-1,b,0)
        print(st)
