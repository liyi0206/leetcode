#55 jump game
class Solution(object):
    def canJump(self,nums): #o(n)
        if not nums: return False
        maxJump=nums[0]
        for i in range(1,len(nums)):
            maxJump-=1
            if maxJump<0: return False
            maxJump=max(maxJump,nums[i])
        return True
    
a=Solution()
print a.canJump([2,3,1,1,4]) #T
print a.canJump([3,2,1,0,4]) #F

#45 Jump Game II
class Solution(object):
    def jump(self,nums):
        maxj,maxn=0,0
        res=0
        for i in range(len(nums)-1):
            maxn=max(maxn,i+nums[i])
            if i==maxj: 
                maxj=maxn
                res+=1
        return res
        
# candy
# gas station