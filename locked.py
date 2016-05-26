# 255 Verify Preorder Sequence in Binary Search Tree
"""
Given an array of numbers, verify whether it is the correct 
preorder traversal sequence of a binary search tree.
You may assume each number in the sequence is unique.

Follow up:
Could you do it using only constant space complexity?
"""
class Solution1(object): #O(n) time, O(n) stack
    # @param {integer[]} preorder
    # @return {boolean}
    def verifyPreorder(self, preorder):
        inorder = []
        stack = []
        for p in preorder:
            if inorder and p < inorder[-1]:
                return False
            while stack and p > stack[-1]:
                inorder.append(stack.pop())
            stack.append(p)
        return True
        
class Solution2(object): #O(n) time, O(n) stack
    def verifyPreorder(self, preorder):
        low = -1
        stack = []
        for p in preorder:
            if p<low: return False
            while stack and p>stack[-1]: low=stack.pop()
            stack.append(p)
        return True
        
class Solution3(object): #O(n) time, O(1) stack
    def verifyPreorder(self, preorder):
        low=-1
        i = -1
        for p in preorder:
            if p<low: return False
            while i>=0 and p>preorder[i]:
                low = preorder[i]
                i-=1
            i+=1
            preorder[i]=p
        return True


# 270 Closest Binary Search Tree Value
# 272 Closest Binary Search Tree Value II
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution270(object):
    def closestValue(self,root,target):
        if not root: return None
        if root.val==target: return 0
        elif root.val<target: 
            closest=self.closestValue(root.right,target)
        else:
            closest=self.closestValue(root.left, target)
        res=target-root.val
        if closest and abs(closest)<abs(res): return closest
        return res

class Solution272(object): #smart solution
    def closestValue(self,root,target,k):
        self.res=[]
        self.collect(root,target,k)
        return self.res
        
    def collect(self,node,target,k):
        if not node: return
        
        self.collect(node.left, target,k)
        
        if len(self.res)==k:
            if abs(node.val-target)<abs(self.res[0]-target): 
                self.res=self.res[1:]
            else: return
        self.res.append(node.val)
        
        self.collect(node.right,target,k)

# 277 Find the Celebrity
class Solution:
    def find(self,n): #o(n)
        p1,p2=0,1
        #res=-1 #idx for celebrity
        while p2<len(n):
            if not self.helper(p1,p2): p2+=1 #p2 is not celebrity
            else: p1=p2 #p1 is not celebrity
        if p2==len(n)-1: return p1
        #return res
        
    def helper(self,a,b):
        "if a knows b, return True; o/w False"
        pass

# 293 Flip Game - Write a function to compute all possible states of the string after one valid move.
# 294 Flip Game II - Write a function to determine if the starting player can guarantee a win.
# Derive your algorithm's runtime complexity.
class Solution293(object):
    def generateStatus(self,s):
        res=[]
        for i in range(len(s)-1):
            if s[i]==s[i+1]=="+":
                res.append(s[:i]+"--"+s[i+2:])
        return res
class Solution294(object): # time o(n!!)
    def __init__(self):
        self.visited={}
     
    def canWin1(self,s):  # with memorization
        if len(s)<2: return False
        if s in self.visited: return self.visited[s]
        for n in range(len(s)-1):
            if s[n:n+2]=='++' and not self.canWin1(s[:n]+'--'+s[n+2:]):
                self.visited[s] = True
                return True
        self.visited[s] = False
        return False
             
    def canWin2(self,s):  # simple version
        if len(s)<2: return False
        for n in range(len(s)-1): #not the other player can win
            if s[n:n+2]=='++' and not self.canWin2(s[:n]+'--'+s[n+2:]):
                return True
        return False

#a=Solution293()
#print a.generateStatus("++++") #["--++","+--+","++--"]
#b=Solution294()
#print b.canWin1("++++") #True
#print b.canWin2("++++") #True

# 320 Generalized Abbreviation ****
"""
Write a function to generate the generalized abbreviations of a word.
Example: Given word = "word", return the following list (order does not matter):
["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", 
 "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]
"""
class Solution(object): # bit manipulation, o(2**n * word_length)
    def abbr1(self,word):
        res,N=[],len(word)
        for i in range((1<<N)): res.append(self.process(i,word,N))
        return res
        
    def process(mask,word,N):
        x = ''
        last = -1
        for n in range(N):
            c = mask&(1<<n)
            if c: # is letter
                x+=(str(n-last-1) if n>last+1 else '')+word[n]
                last = n
        if last<N-1: x+=str(N-1-last)
        return x
                     
    def abbr2(self,word): # backtracking, o(2**n)
        self.word,self.N = word,len(word)   
        self.res = []
        self.bt('',0,0)
        return self.res
        
    def bt(self,cur,n,count): 
        #print "dfs",cur,n,count
        if n==self.N:
            self.res.append(cur+str(count) if count>0 else cur)
            return     
        self.bt(cur,n+1,count+1)
        self.bt(cur+(str(count) if count>0 else '')+self.word[n],n+1,0)

#a=Solution()
#print a.abbr2("word")

# 341 Flatten Nested List Iterator
#Given a nested list of integers, implement an iterator to flatten it.
#Each element is either an integer, or a list -- whose elements may also be integers or other lists.

#from matplotlib.cbook import flatten 
#tmp=flatten([1,2,[3,4,5,[],[6,7,[8,9],10]],[[]],11,12])
#for i in range(12): print tmp.next()

class DeepIterator(): # input is iter of numbers
    def __init__(self,it):
        self.it = it
        self.top = None
        self.stk = [it]
         
    #def __iter__(self):
    #    return self
     
    def next(self):
        if not self.hasNext(): return None
        res,self.top = self.top,None
        return res
     
    def hasNext(self):
        if self.top: return True
        while self.stk:
            peek = self.stk[-1]
            try:
                nxt = peek.next()
                if type(nxt)==int:
                    self.top = nxt
                    return True
                else: self.stk.append(nxt)
            except StopIteration: self.stk.pop()
        return False

iter_nums=iter([1,2,iter([3,4,5,iter([]),iter([6,7,iter([8,9]),10])]),iter([iter([])]),11,12])
di=DeepIterator(iter_nums)
for i in range(12): print di.next()

class DeepIterator2(): # input is list of numbers, keep stk of array and inded
    def __init__(self,nestedList):
        self.stack = [[nestedList,0]]
    
    def hasnext(self):
        while self.stack:
            nestedList,i = self.stack[-1]
            if i==len(nestedList): self.stack.pop()
            else:
                x=nestedList[i]
                if type(x)==int: return True
                else:
                    self.stack[-1][-1]+=1
                    self.stack.append([x,0])
            
        return False
        
    def next(self):
        if not self.hasnext(): return None
        nestedList,i = self.stack[-1]
        self.stack[-1][1]+=1
        return nestedList[i]
     
nums=[1,2,[3,4,5,[],[6,7,[8,9],10]],[[]],11,12]
di=DeepIterator2(nums)
for i in range(12): print di.next()