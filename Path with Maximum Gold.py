n,m=list(map(int,input().split()))
grid=[]
for i in range(n):
    g=list(map(int,input().split()))
    grid.append(g)

def done(grid,j,k,s,fin):
    global l
    global tfin
    if -1<j<n and -1<k<m:
        if grid[j][k]!=0 and [j,k] not in s:
           done(grid, j - 1, k, s+[[j,k]], fin+[grid[j][k]])
           done(grid, j , k - 1, s+[[j,k]], fin+[grid[j][k]])
           done(grid, j + 1, k,s+[[j,k]], fin+[grid[j][k]])
           done(grid, j , k + 1, s+[[j,k]], fin+[grid[j][k]])
           fin.append(grid[j][k])
           s.append([j,k])
           if sum(fin)>l:
               l=sum(fin)
               tfin=fin[:]


l=0
s = []
tfin=[]
for j in range(n):
    for k in range(m):
        if grid[j][k]!=0 and [j,k] not in s:
            fin = []
            s = []
            done(grid,j,k,s,fin)
print(sum(tfin))
