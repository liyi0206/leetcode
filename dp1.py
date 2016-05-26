# 53. Maximum Subarray
# could be improved to have only 1+1 extra space
class Solution(object):
    def maxSubArray(self,nums):
        dp=[nums[0]]+[0]*(len(nums)-1)
        for i in range(1,len(nums)):
            dp[i]=max(nums[i],dp[i-1]+nums[i])
        return max(dp)
        
#a=Solution()
#print a.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) #6
        
#152. Maximum Product Subarray
# abs(maxdp[i-1]) and abs(mindp[i-1]) must be >1, as all are integers
# could be improved to have only 2+1 extra space
class Solution(object):
    def maxProduct(self, nums):
        maxdp=[nums[0]]+[None]*(len(nums)-1)
        mindp=[nums[0]]+[None]*(len(nums)-1)
        for i in range(1,len(nums)):
            maxdp[i]=max(nums[i],maxdp[i-1]*nums[i],mindp[i-1]*nums[i])
            mindp[i]=min(nums[i],maxdp[i-1]*nums[i],mindp[i-1]*nums[i])
        return max(maxdp)

#a=Solution()
#print a.maxProduct([2,3,-2,4]) #6

# 70. Climbing Stairs
class Solution(object):
    def climbStairs(self, n):
        dp= [1,1]
        while len(dp)<=n: dp.append(dp[-1]+dp[-2])
        return dp[n]

# 91. Decode Ways
class Solution(object):        
    def numDecodings(self,s): #DP
        if not s: return 0
        pp,p=0,1
        for i in range(len(s)):
            cur = 0
            if s[i]!='0': cur=p
            if i>0 and (s[i-1]=="1" or (s[i-1]=="2" and s[i] <="6")): cur+=pp
            p,pp=cur,p
        return p
        
    def is_valid(self,s):
        if 1<=int(s)<=26 and s[0]!='0': return True
        return False
  
#198 House Robber
#213 House Robber II

#300 Longest Increasing Subsequence
#(1) o(n^2) time
#dp[x] = max(dp[x], dp[y] + 1), where y < x, nums[x] > nums[y]
#(2) o(nlogn) time
#keep an asc array, binary search for the loc of next elem.
#if loc in array, replace it. if loc=len(array), add it.
#(smallify the existing elems, extend the array if met larger elem)

#334. Increasing Triplet Subsequence
#keep 2 value, for the first two elem in the increasing triplet
#update 1st when met smallest, update 2nd when met smaller, otherwise return true
