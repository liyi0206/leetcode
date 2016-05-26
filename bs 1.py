#I. Basics
#35. Search Insert Position - distinct elem. return l
class Solution(object):
    def searchInsert(self,nums,target):
        l,h=0,len(nums)-1
        while l<=h:
            m=l+(h-l)/2
            if nums[m]==target: return m
            elif nums[m]<target:l=m+1
            else: h=m-1
        return l

#a=Solution()
#print a.searchInsert([1,3,5,6], 5)
#print a.searchInsert([1,3,5,6], 2)
#print a.searchInsert([1,3,5,6], 7)
#print a.searchInsert([1,3,5,6], 0)

#34. Search for a Range - dup elem. 
# remember to check m1>=0 and m2<len(nums)
class Solution(object):
    def searchRange(self,nums,target):
        l,h=0,len(nums)-1
        while l<=h:
            m=l+(h-l)/2
            if nums[m]==target:
                m1,m2=m,m
                while m1>=0 and nums[m1]==target: m1-=1
                while m2<len(nums) and nums[m2]==target: m2+=1
                return [m1+1,m2-1]
            elif nums[m]<target:l=m+1
            else: h=m-1
        return [-1,-1]
        
#a=Solution()
#print a.searchRange([5, 7, 7, 8, 8, 10],8)

#74. Search a 2D Matrix - could treat as an array
# remember to /b not /a
class Solution(object):
    def searchMatrix(self,matrix,target):
        a,b=len(matrix),len(matrix[0])
        l,h=0,a*b-1
        while l<=h:
            m=l+(h-l)/2
            if matrix[m/b][m%b]==target: return True
            elif matrix[m/b][m%b]<target: l=m+1
            else: h=m-1
        return False
  
matrix=[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]]      
#a=Solution()
#print a.searchMatrix(matrix,3) #true

#33. Search in Rotated Sorted Array - distinct elem
# remember to add condition for nums[l]==nums[m]
# as elems have no dup, such condition only happens when h=l+1
class Solution(object):
    def search(self,nums,target):
        l,h=0,len(nums)-1
        while l<=h:
            m=l+(h-l)/2
            if nums[m]==target: return m
            elif (nums[l]<nums[m] and (target<nums[l] or target>nums[m])) or \
                 (nums[l]>nums[m] and nums[m]<target<nums[l]) or \
                 (nums[l]==nums[m]): l=m+1
            else: h=m-1
        return -1

#a=Solution()
#print a.search([4,5,6,7,0,1,2],6)
#print a.search([4,5,6,7,0,1,2],1)
#print a.search([4,5,6,7,0,1,2],4)
#print a.search([1,3],3)

#81. Search in Rotated Sorted Array II (*) - dup elem - return T/F
# add if nums[m]==nums[l]==nums[h]: l,h = l+1,h-1
class Solution(object):
    def search(self,nums,target):
        l,h=0,len(nums)-1
        while l<=h:
            m=l+(h-l)/2
            if nums[m]==target: return True
            elif nums[m]==nums[l]==nums[h]: l,h = l+1,h-1
            elif (nums[l]<nums[m] and (target<nums[l] or target>nums[m])) or \
                 (nums[l]>nums[m] and nums[m]<target<nums[l]) or \
                 (nums[l]==nums[m]): l=m+1
            else: h=m-1
        return False
        
# I think it doesn't matter if dup occur on m, 
# or in ([l,m] and nums[l]!=nums[m]) or ([m,h] and nums[m]!=nums[h])
# or in ([l,m] and nums[l]==nums[m] but nums[m]!=nums[h]) or
#       ([m,h] and nums[m]==nums[h] but nums[l]!=nums[m])
# only when nums[l]==nums[m]==nums[h] could be all elems are the same,
# or the increasing part is in [l,m] or [m,h]


#153. Find Minimum in Rotated Sorted Array - distinct elem
class Solution(object):
    def findMin(self,nums):
        l,h=0,len(nums)-1
        while l<=h:
            m=l+(h-l)/2
            if nums[l]<nums[m]<nums[h]: return nums[l]
            elif nums[l]<nums[m] and nums[m]>nums[h]: l=m+1
            elif nums[l]==nums[m]: return min(nums[l],nums[h])
            else: h=m
        return nums[l] 

a=Solution()
print a.findMin([4,5,6,7,0,1,2])
print a.findMin([5,6,7,0,1,2,3,4])

#154. Find Minimum in Rotated Sorted Array II - dup elem


#II, real world problems
#275. H-Index II (*)

#278. First Bad Version
#315. Count of Smaller Numbers After Self (*) - use l part of search in range algo


#III. strict constraints
#162. Find Peak Element - o(logn) time, could return any peak elem
#(1) could prove there is always a solution, when -1 and n are -inf, and no neighbors are the same
#(2) if scan once, worst case, asc, return last. o(n). but usually could return first peak fast
#(3) to ensure o(logn) time, binary search, when nums[m]<nums[m+1], regard [m+1,h] as new array,
#with both ends -inf. otherwise, [l,m] is such new array, with both ends -inf.


#287. Find the Duplicate Number (revisit) - o(n^2) time, o(1) extra space, no change in input