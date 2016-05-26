#I. Bit Manipulation Basics
#136. Single Number - use of ^ (xor), python version needs
class Solution(object):
    def singleNumber(self,nums):
        res=0
        for a in nums: res^=a
        return res

#137. Single Number II (*) - use of AND *******
class Solution(object):
    def singleNumber(self,nums): #only work for positive
        res=0
        for i in range(32):
            cnt=[1 for num in nums if (num>>i)&1]
            if cnt%3: res+=(1<<i)
        return res        

#260. Single Number III (*)
class Solution(object):
    def singleNumber(self,nums):
        xor=0
        for a in nums: xor^=a
        
        mask=0
        for i in range(32):
            if (xor>>i)&1: 
                mask=(1<<i)
                break #optional
        
        xor0,xor1=0,0
        for a in nums:
            if a&mask: xor1^=a
            else: xor0^=a
            
        return [xor0,xor1]
            
#a=Solution()
#print a.singleNumber([1, 2, 1, 3, 2, 5])

#201. Bitwise AND of Numbers Range (*) - use AND out of memory, use <0 and n&(n-1) == 0
class Solution(object):
    def rangeBitwiseAndME(self,m,n): #MemoryError
        res=m
        for i in range(m+1,n+1): res&=i
        return res
        
    def rangeBitwiseAnd(self,m,n):
        bit=0
        while m!=n: m,n,bit=m>>1,n>>1,bit+1
        return m<<bit  

a=Solution()
print a.rangeBitwiseAnd(5,7)

#268. Missing Number - constraint: o(n) time, o(1) extra space.
# (1) could use sum as well
# (2) if have o(n) space, 
class Solution(object):
    def missingNumber(self,nums):
        xor1,xor2=0,0
        for i in range(len(nums)+1): xor1^=i
        for num in nums: xor2^=num
        return xor1^xor2

#318. Maximum Product of Word Lengths (*) - make words 26 binary bits, use AND to compare dup letters
class Solution(object):
    def maxProduct(self, words):
        nums=[0]*len(words)
        for i,word in enumerate(words):
            for c in word:
                nums[i]|=1<<(ord(c)-ord('a'))
        res=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]&nums[j]==0: 
                    res=max(res,len(words[i])*len(words[j]))    
        return res

#289. Game of Life - in-place, use &1 to examine current status, 
#use |=2 to record next status, use <<=1 to roll over to next status.


#III, python tricks
#190. Reverse Bits
class Solution(object):
    def reverseBits(self, n):
        return int("".join(list(reversed(bin(n)[2:].zfill(32)))),2)

#191. Number of 1 Bits
class Solution(object):
    def hammingWeight(self, n):
        return sum(1 for c in bin(n) if c=="1")