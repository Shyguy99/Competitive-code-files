from collections import defaultdict


def dfs( temp, v, vis):
        global li
        st = []

        st.append(v)

        while (len(st)):
            s = st[-1]
            st.pop()

            if (not vis[s]):
                temp+=li[s]
                vis[s] = True

            for node in ga[s]:
                if (not vis[node]):
                    st.append(node)
        return temp
def addedge(v, w):
        global ga
        ga[v].add(w)
        ga[w].add(v)


vis = []
n=int(input())
ga=defaultdict(set)
li=list(map(int,input().split()))
q=int(input())
for i in range(q):
    a,b=map(int,input().split())
    addedge(a-1,b-1)
vis=[False for i in range(n)]
maxx=0
for ver in range(n):
    if vis[ver] == False:
        temp =0
        maxx=max(maxx,(dfs(temp, ver, vis)))
print(maxx)



