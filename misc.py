#179. Largest Number
class Solution(object):
    def largestNumber(self,nums):
        if not nums: return ''
        nums=sorted([str(a) for a in nums], cmp=self.compare)
        res=''.join(nums).lstrip('0')
        return res or '0'
            
    def compare(self,a,b):
        return [1, -1][a+b > b+a]
        
a=Solution()
print a.largestNumber([3,30,34,5,9]) #9534330


#11 Container With Most Water


#42 Trapping Rain Water