#41. First Missing Positive - o(n) time, constant space
#(1) nums[nums[i]-1],nums[i] = nums[i],nums[nums[i]-1] - swap order matters
#(2) else: i+=1 - if swap, stay at i to continue swap until not possible
#thus, no need to specify nums[i]!=i+1 in if clause.


#73. Set Matrix Zeroes - o(mn) time, constant space
#scan first row/col (store in 2 extra space), then scan the rest (store in first row/col). update the rest, update first row/col.


#118. Pascal's Triangle
#119. Pascal's Triangle II
#169. Majority Element
#229. Majority Element II - scan twice, first to create hash dashboard, second to confirm >1/3

#189. Rotate Array - swap,swap,swap

#228. Summary Ranges - dummy tail

#238. Product of Array Except Self - scan twice forward and backward, for prod