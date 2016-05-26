#I. water problems - 2p walking closer
#11. Container With Most Water (*) - find range with max vol
class Solution(object):
    def maxArea(self,height):
        pass

#42. Trapping Rain Water (*) - find total vol
class Solution(object):
    def trap(self, height):
        maxl,maxr,tmp=[],[],0
        for i,h in enumerate(height):
            if h>tmp: tmp=h
            maxl.append(tmp)
        tmp=0
        for i in range(len(height)-1,-1,-1):
            if height[i]>tmp: tmp=height[i]
            maxr.append(tmp)
        res=0
        for i,h in enumerate(height):
            area=min()*(h2-h1)
            
        return res
        

#II. sum problems - 2p walking closer
#15. 3Sum
#16. 3Sum Closest
#259. 3Sum Smaller




#III. Basics - 2p random walk
#26. Remove Duplicates from Sorted Array () - no 2 dups.
# one pointer to scan, switch dup with next new, 
# other pointer to stay on distinct counts


#80. Remove Duplicates from Sorted Array II () - no 3 dups


#75. Sort Colors (*) - o(n) time, o(1) extra space
# two pointers from start and end, and a free i from start.
# p1 represent the first non 0 elem idx from left,
# p2 represent the first non 2 elem idx from right,
# i represent the first unknown non 1 elem idx from left
# each time when I meets 0 or 2, exchange with val in p1 or p2, p1++ (i++) or p2--
# otherwise i meets 1 and i++


#IV. python tricks
#27. Remove Element
#88. Merge Sorted Array - nums1 has enough space, modify nums1 in-place, put backward
#125. Valid Palindrome
#283. Move Zeroes