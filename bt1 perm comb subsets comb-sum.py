#chenxing dfs question
#329. Longest Increasing Path in a Matrix

#235. Lowest Common Ancestor of a Binary Search Tree
#236. Lowest Common Ancestor of a Binary Tree My Submissions Question (**)

#memorization

class Solution(object):
    def permute(self,nums): #o(n!)
        self.nums,self.n=nums,len(nums)
        self.res=[]
        self.bt(0,[nums[0]])
        return self.res
            
    def bt(self,i,tmp):
        if i==self.n-1: 
            self.res.append(tmp)
            return
        for k in range(i+2):
            self.bt(i+1,tmp[:k]+[self.nums[i+1]]+tmp[k:])
            
    def permute_iter(self,nums):
        cur=[[]]
        for num in nums:
            next=[]
            for sol in cur:
                for i in range(len(sol)+1):
                    next.append(sol[:i]+[num]+sol[i:])
            cur=next
        return cur
    
a=Solution()
print a.permute_iter([1,2,3])

class Solution12(object):
    def permuteUnique(self,nums):
        self.nums,self.n=nums,len(nums)
        self.res=[]
        self.bt(0,[nums[0]])
        return self.res

    def bt(self,i,tmp):
        if i==self.n-1:
            if tmp not in self.res: 
                self.res.append(tmp)
            return
        for k in range(i+2):
            self.bt(i+1,tmp[:k]+[self.nums[i+1]]+tmp[k:])
            
    def permuteUnique_iter(self,nums):
        cur=[[]]
        for num in nums:
            next=[]
            for sol in cur:
                for i in range(len(sol)+1):
                    tmp=sol[:i]+[num]+sol[i:]
                    if tmp not in next: next.append(tmp)
            cur=next
        return cur

a=Solution12()
print a.permuteUnique_iter([1,1,2])

class Solution2(object):
    def combine(self,n,k): #o(n choose k)
        self.n,self.k=n,k
        self.res=[]
        for i in range(1,n+1):
            self.bt(i,[i])
        return self.res
        
    def bt(self,i,tmp):
        if len(tmp)==self.k:
            self.res.append(tmp)
            return
        for j in range(i+1,self.n+1):
            self.bt(j,tmp+[j])

#a=Solution2()
#print a.combine(4,2)

class Solution3(object):
    def subsets(self,nums): #o(2^n)
        self.nums,self.n=sorted(nums),len(nums)
        self.res=[[]]
        for i in range(self.n):
            self.bt(i,[self.nums[i]])
        return self.res
        
    def bt(self,i,tmp):
        self.res.append(tmp)
        for j in range(i+1,self.n):
            self.bt(j,tmp+[self.nums[j]])
        
#a=Solution3()
#print a.subsets([1,2,3])
#print a.subsets([4,1,0])

class Solution32(object):
    def subsetsWithDup(self,nums):
        self.nums,self.n=sorted(nums),len(nums)
        self.res=[[]]
        for i in range(self.n):
            self.bt(i,[self.nums[i]])
        return self.res
        
    def bt(self,i,tmp):
        if tmp not in self.res:
            self.res.append(tmp)
        for j in range(i+1,self.n):
            self.bt(j,tmp+[self.nums[j]])
            
#a=Solution32()
#print a.subsetsWithDup([1,2,2])