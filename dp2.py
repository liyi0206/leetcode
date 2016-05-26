#62. Unique Paths - f(m,n) = f(m-1,n)+f(m,n-1)
#63. Unique Paths II - f(m,n) = f(m-1,n)+f(m,n-1)
#64. Minimum Path Sum - f(m,n) += min(f(m-1,n),f(m,n-1))


# ABSTRACT
#72. Edit Distance (*) - f(m,n) = min(f(m-1,n),f(m,n-1),f(m-1,n-1))
class Solution(object):
    def editDistance(self,word1,word2):
        dp=[[0]*(len(word2)+1) for i in range(len(word1)+1)]
        for i in range(1,len(word1)+1): dp[i][0]=i
        for i in range(1,len(word2)+1): dp[0][i]=i
        for i in range(1,len(word1)+1):
            for j in range(1,len(word2)+1):
                if word1[i-1]==word2[j-1]:
                    dp[i][j]=min(dp[i-1][j-1],dp[i][j-1]+1,dp[i-1][j]+1)
                else: 
                    dp[i][j]=min(dp[i-1][j-1]+1,dp[i][j-1]+1,dp[i-1][j]+1)
        #for l in dp: print l
        return dp[-1][-1]

#a=Solution()
#print a.editDistance("SAND","SEA") #3

# TABLE FILLING
#120. Triangle (*) - f(m,n) = min(f(m-1,n-1),f(m-1,n))+d(m,n)
class Solution(object):
    def minimumTotal(self,triangle):
        dp=[[0]*(len(triangle[i])) for i in range(len(triangle))]
        dp[0][0]=triangle[0][0]
        for i in range(1,len(triangle)):
            dp[i][0]=dp[i-1][0]+triangle[i][0]
            dp[i][-1]=dp[i-1][-1]+triangle[i][-1]        
        for i in range(2,len(triangle)):
            for j in range(1,len(triangle[i])-1):
                dp[i][j]=min(dp[i-1][j-1],dp[i-1][j])+triangle[i][j]
        #for l in dp: print l
        return min(dp[-1])
        
#triangle=[
#     [2],
#    [3,4],
#   [6,5,7],
#  [4,1,8,3]]
#a=Solution()
#print a.minimumTotal(triangle)

#221. Maximal Square - dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1

# TABLE FILLING
#174 Dungeon Game (*)
class Solution(object):
    def calculateMinimumHP(self, dungeon):
        n,m=len(dungeon),len(dungeon[0])
        dp=[[0]*m for i in range(n)]
        dp[-1][-1]=max(1-dungeon[-1][-1],1)
        for i in range(n-2,-1,-1):
            dp[i][m-1]=max(dp[i+1][m-1]-dungeon[i][m-1],1)
        for j in range(m-2,-1,-1):
            dp[n-1][j]=max(dp[n-1][j+1]-dungeon[n-1][j],1)        
        for i in range(n-2,-1,-1):
            for j in range(m-2,-1,-1):
                dp[i][j]=max(min(dp[i+1][j]-dungeon[i][j],
                                 dp[i][j+1]-dungeon[i][j]),1)
        #for l in dp: print l
        return dp[0][0]
    
#dungeon=[[-2,-3,3],[-5,-10,1],[10,30,-5]]
#a=Solution()
#print a.calculateMinimumHP(dungeon)

# ABSTRACT
#312 Burst Balloons (*)
class Solution(object):
    def maxCoins(self,nums):
        n=len(nums)
        nums=[1]+nums+[1]
        dp=[[0]*(n+2) for i in range(n+2)]
        for k in range(2,n):
            for l in range(1,n-k):
                h=l+k
                for i in range(l,h):
                    dp[l][h]=max(dp[l][l+i]*nums[l+i]*dp[l+i+1][h])
                
        return dp[-1][-1]
                
a=Solution()
print a.maxCoins([3, 1, 5, 8]) #167