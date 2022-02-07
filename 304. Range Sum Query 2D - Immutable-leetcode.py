class NumMatrix:

    def __init__(self, matrix):

        n = len(matrix)
        m = len(matrix[0])
        self.fmat = [[0 for i in range(m)] for j in range(n)]
        self.fmat[0][0] = matrix[0][0]
        for i in range(1, m):
            self.fmat[0][i] = self.fmat[0][i - 1] + matrix[0][i]

        for j in range(1, n):
            self.fmat[j][0] = self.fmat[j-1][0] + matrix[j][0]

        for i in range(1, n):
            for j in range(1, m):
                self.fmat[i][j] = self.fmat[i][j - 1] + self.fmat[i - 1][j] + matrix[i][j] - self.fmat[i - 1][j - 1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int):
        k = self.fmat[row2][col2]
        print(k,"k")
        if col1 > 0:
            f1 = self.fmat[row2][col1 - 1]
            print(f1,"f1")
            k -= f1
        if row1 > 0:
            f2 = self.fmat[row1 - 1][col2]
            print(f2,"f2")
            k -= f2
        if row1 - 1 >= 0 and col1 - 1 >= 0:
            f3 = self.fmat[row1 - 1][col1 - 1]
            print(f3,"f3")
            k += f3
        return k
m=[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]
ob=NumMatrix(m)
for i in range(len(ob.fmat)):
    print(*ob.fmat[i])

print(ob.sumRegion(2,1,4,3))
# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)