import numpy as np
for _ in range(int(input())):
    n,m,q=list(map(int,input().split()))
    mat=np.zeros((n,m))
    coun=0
    for i in range(q):
        x,y=list(map(int,input().split()))
        np.add.at(mat[x-1],range(0,m),1)
        np.add.at(mat[:,y-1],range(0,n),1)
        print(mat)
        coun=0
        for i in mat:
           for j in i:
               if j%2!=0:
                   coun+=1
        print(coun)