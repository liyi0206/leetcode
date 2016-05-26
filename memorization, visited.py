#Longest Increasing Path in a Matrix
class Solution(object):
    def longestIncreasingPath(self,matrix):
        if not matrix: return 0
        self.matrix,self.n,self.m=matrix,len(matrix),len(matrix[0])
        self.dp=[[0]*self.m for i in range(self.n)]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if self.dp[i][j]==0:
                    self.bt(i,j)
        print self.dp
        return max([max(a) for a in self.dp])
        
    def bt(self,x,y):
        for dx,dy in [[-1,0],[1,0],[0,-1],[0,1]]:
            nx,ny=x+dx,y+dy
            if 0<=nx<self.n and 0<=ny<self.m and \
                self.matrix[nx][ny]<self.matrix[x][y]:
                    if self.dp[nx][ny]==0: self.bt(nx,ny)
                    self.dp[x][y]=max(self.dp[x][y],self.dp[nx][ny]+1)
        self.dp[x][y]=max(self.dp[x][y],1)
        
nums1 = [
  [9,9,4],
  [6,6,8],
  [2,1,1]
]
nums2 = [
  [3,4,5],
  [3,2,6],
  [2,2,1]
]
#a=Solution()
#print a.longestIncreasingPath(nums1)
#print a.longestIncreasingPath(nums2)

#37. Sudoku Solver (*) 
class Solution(object):
    def solveSudoku(self,board):
        self.board=board #board is visited
        self.bt()
                    
    def bt(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j]=='.':
                    for num in '123456789':
                        self.board[i][j]=num
                        if self.checkValid(i,j,num) and self.bt(): return True
                        self.board[i][j]='.'
                    return False 
                    #if there are '.' and not valid at some point, return False
        return True # when there is no more '.' return True
        
    def checkValid(self,x,y,val):
        for i in range(9):
            if i!=y and self.board[x][i]==val: return False
            if i!=x and self.board[i][y]==val: return False
        for i in range(3):
            for j in range(3):
                if ((x/3)*3+i!=x or (y/3)*3+j!=y) and \
                    self.board[(x/3)*3+i][(y/3)*3+j]==val: return False
        return True

tmp=[
        '53..7....',
        '6..195...',
        '.98....6.',
        '8...6...3',
        '4..8.3..1',
        '7...2...6',
        '.6....28.',
        '...419..5',
        '....8..79'
    ]
board=[[a[j] for j in range(9)] for a in tmp]
a=Solution()
a.solveSudoku(board)

#79. Word Search (*)
class Solution(object): #TLE
    def exist(self,board,word):
        self.board,self.n,self.m=board,len(board),len(board[0])
        self.visited=[[0]*self.m for a in range(self.n)]
        self.res=False
        for i in range(self.n):
            for j in range(self.m):
                if not self.visited[i][j]:
                    self.bt(i,j,word)
        return self.res
                    
    def bt(self,x,y,word):
        if len(word)==1 and self.board[x][y]==word:
            self.res=True
            return
        elif self.board[x][y]==word[0]:    
            for dx,dy in ((-1,0),(1,0),(0,-1),(0,1)):
                nx,ny=x+dx,y+dy
                if 0<=nx<self.n and 0<=ny<self.m and self.visited[nx][ny]==0:
                    self.visited[nx][ny]=1
                    self.bt(nx,ny,word[1:])
                    self.visited[nx][ny]=0
     
class Solution2(object):  #TLE - where should I prune??
    def exist(self,board,word):
        self.board,self.n,self.m=board,len(board),len(board[0])
        self.visited=[[0]*self.m for a in range(self.n)]
        self.res=False
        for i in range(self.n):
            for j in range(self.m):
                if self.bt(i,j,word): return True
        return False
                    
    def bt(self,x,y,word):
        if len(word)==0: return True
        if not (0<=x<self.n and 0<=y<self.m and self.visited[x][y]==0 \
                and self.board[x][y]==word[0]): return False
        
        self.visited[x][y]=1
        for dx,dy in ((-1,0),(1,0),(0,-1),(0,1)):
            nx,ny=x+dx,y+dy
            if self.bt(nx,ny,word[1:]): return True
        self.visited[x][y]=0

board=[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']]
a=Solution2()
#print a.exist(board,"ABCCED")
#print a.exist(board,"SEE")
#print a.exist(board,"ABCB")

#200. Number of Islands (*)
class Solution(object):
    def numIslands(self,grid):
        if not grid: return 0
        self.grid,self.n,self.m=grid,len(grid),len(grid[0])
        res=0
        for i in range(self.n):
            for j in range(self.m):
                if self.grid[i][j]=='1':
                    self.bt(i,j)
                    res+=1
        #print self.grid
        return res
                
    def bt(self,x,y):
        if self.grid[x][y]!='1': return
        self.grid[x][y]='2'
        for dx,dy in ((-1,0),(1,0),(0,-1),(0,1)):
            nx,ny=x+dx,y+dy
            if 0<=nx<self.n and 0<=ny<self.m:
                self.bt(nx,ny)

input1=["11110",
        "11010",
        "11000",
        "00000"]
grid1=[]
for item in input1: grid1.append([c for c in item])

input2=["11000",
        "11000",
        "00100",
        "00011"]
grid2=[]
for item in input2: grid2.append([c for c in item])
a=Solution()
#print a.numIslands(grid1)
#print a.numIslands(grid2)

#241. Different Ways to Add Parentheses (*)
#301. Remove Invalid Parentheses (*)