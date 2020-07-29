def solution(map):
    ch = 0
    k = []
    global tt
    tt = [0]
    i = len(map)
    j=len(map[0])
    d=[]
    def done(map, i, j, k, ch,d):
        t=min(tt)
        if i==0 and j == 0:
            tt.append(len(k) + 1)
            if tt[0]==0:
                tt.remove(tt[0])

        elif i >= 0 and i <= len(map) - 1 and j >= 0 and j <= len(map[0]) - 1 and (t==0 or t>len(k)+1+i+j):
            if map[i][j] == 1 and ch != 1 and [i,j] not in d:
                done(map, i - 1, j, k + [1], ch+1,d+[[i,j]])
                done(map, i, j + 1, k + [1], ch+1,d+[[i,j]])
                done(map, i + 1, j, k + [1], ch+1,d+[[i,j]])
                done(map, i, j - 1, k + [1], ch+1,d+[[i,j]])
            elif map[i][j]==0 and  [i,j] not in d:
                done(map, i - 1, j, k + [1], ch,d+[[i,j]])
                done(map, i, j + 1, k + [1], ch,d+[[i,j]])
                done(map, i + 1, j, k + [1], ch,d+[[i,j]])
                done(map, i, j - 1, k + [1], ch,d+[[i,j]])


    done(map, i - 1, j - 1, k, ch,d)
    return min(tt)
map=[[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]
print(solution(map))

