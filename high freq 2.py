#94. Binary Tree Inorder Traversal
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        res=[]
        stack=[]
        cur=root
        while cur or stack:
            if cur:
                stack.append(cur)
                cur=cur.left
            else:
                parent=stack.pop()
                res.append(parent.val)
                cur=parent.right
        return res 
        
#144. Binary Tree Preorder Traversal
class Solution(object):
    def preorderTraversal(self, root):
        res=[]
        stack=[]
        cur=root
        while cur or stack:
            if cur:
                res.append(cur.val)
                stack.append(cur)
                cur=cur.left
            else:
                parent=stack.pop()
                cur=parent.right
        return res        

#235. Lowest Common Ancestor of a Binary Search Tree
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        cur=root
        pval,qval=min(p.val,q.val),max(p.val,q.val)
        while cur:
            if pval<=cur.val<=qval: return cur
            elif cur.val<pval: cur=cur.right
            else: cur=cur.left
            
#236. Lowest Common Ancestor of a Binary Tree
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if not root: return None
        if root==p or root==q: return root ##return node itself, not node.val
        left =self.lowestCommonAncestor(root.left,p,q)
        right=self.lowestCommonAncestor(root.right,p,q)
        if not left: return right
        elif not right: return left
        else: return root

#270. Closest Binary Search Tree Value 
class Solution(object):
    def closestValue(self, root, target):
        res=root.val ## better than a random large number
        cur=root
        while cur:
            if cur.val==target: return cur.val
            if abs(cur.val-target)<abs(res-target): res=cur.val
            if cur.val<target: cur=cur.right
            else: cur=cur.left
        return res
            
#272. Closest Binary Search Tree Value II
class Solution(object):
    def closestKValues(self, root, target, k):
        array1,array2=[],[]
        stack=[]
        cur=root
        while cur or stack:
            if cur:
                stack.append(cur)
                cur=cur.left
            else:
                parent=stack.pop()
                if parent.val<=target: 
                    array1.append(parent.val)
                else: 
                    # append here and pop(0) later is more efficient,
                    # as not all vals needs to pop.
                    array2.append(parent.val) 
                    if len(array2)>k: break
                cur=parent.right
        #print array1, array2
        
        res=[]
        for i in range(k):
            if not array1 and not array2: break  #not going to happen
            elif not array2: res.append(array1.pop())
            elif not array1: res.append(array2.pop(0))
            elif target-array1[-1]<array2[0]-target: res.append(array1.pop())
            else: res.append(array2.pop(0))
            
        ### best - assume k is always valid, that is: k <= total nodes.
        #for i in range(k):
        #    if not res2 or (res1 and target-res1[-1]<res2[-1]-target): 
        #        res.append(res1.pop())
        #    else: res.append(res2.pop())
        
        return res
        
#root=TreeNode(2)
#root.left =TreeNode(1)
#root.right=TreeNode(4)
#root.right.left =TreeNode(3)
#root.right.right=TreeNode(5)
#a=Solution()
#print a.closestKValues(root,6,3) #[5,4,3]

#a=Solution()
#print a.closestKValues(TreeNode(1),0,1) 


#146. LRU Cache - see ds implementation
#308. Range Sum Query 2D - Mutable 
class NumMatrix(object):
    def __init__(self, matrix):
        if not matrix: return    ### o/w runtime error
        self.matrix=matrix
        self.n,self.m=len(matrix),len(matrix[0])
        self.tree=[[0]*(self.m+1) for i in range(self.n+1)]
        ### initialize tree
        for x in range(self.n):
            for y in range(self.m):
                self.add(x+1,y+1,matrix[x][y])
        #for l in self.tree: print l
        
    def lowbit(self,x):
        return x&(-x)
        
    def add(self,x,y,val):
        while x<=self.n:     ### not x<n
            z=y
            while z<=self.m: ### not z<n
                self.tree[x][z]+=val
                z+=self.lowbit(z)
            x+=self.lowbit(x)
        
    def sum(self,x,y):
        res=0
        while x>0:      # not matter if x>=0
            z=y
            while z>0:  # not matter if z>=0
                res+=self.tree[x][z]
                z-=self.lowbit(z)
            x-=self.lowbit(x)
        return res
        
    def update(self,i,j,val):
        delta=val-self.matrix[i][j]
        self.add(i+1,j+1,delta)
        self.matrix[i][j]=val     ###
        
    def sumRegion(self,row1,col1,row2,col2):
        return self.sum(row2+1,col2+1) \
             - self.sum(row2+1,col1) \
             - self.sum(row1,col2+1) \
             + self.sum(row1,col1)

#matrix = [
#  [3, 0, 1, 4, 2],
#  [5, 6, 3, 2, 1],
#  [1, 2, 0, 1, 5],
#  [4, 1, 0, 1, 7],
#  [1, 0, 3, 0, 5]]
#numMatrix=NumMatrix(matrix)
#print numMatrix.sumRegion(2,1,4,3) #8
#numMatrix.update(3,2,2)
#print numMatrix.sumRegion(2,1,4,3) #10

#251. Flatten 2D Vector
class Vector2D(object):
    def __init__(self, vec2d):
        self.v=vec2d
        self.x,self.y=0,0

    def next(self):
        if self.hasNext():
            res=self.v[self.x][self.y]
            self.y+=1
            return res
        else: return None
            
    def hasNext(self):
        # jump out of loop when x,y both<limit, or both==limit
        while self.x<len(self.v) and self.y==len(self.v[self.x]):
            self.x+=1
            self.y=0
        if self.x==len(self.v): return False
        else: return True

#281. Zigzag Iterator 
class ZigzagIterator(object):
    def __init__(self, v1, v2):
        self.v=[v1,v2]
        #self.n,self.m=len(v1),len(v2)
        self.x,self.y=0,0
        self.flag0,self.flag1=0,0
        
    def next(self):
        if self.hasNext():
            res=self.v[self.x][self.y]
            if self.flag0==0 and self.flag1==0:
                if self.x==0: self.x=1
                else: self.x,self.y=0,self.y+1
            else: self.y+=1
            return res
        else: return None
        
    def hasNext(self):
        while self.y==len(self.v[self.x]) and (self.flag0==0 or self.flag1==0):
            if self.x==0: 
                self.flag0=1
                self.x=1
            else: 
                self.flag1=1
                self.x=0
                self.y+=1

        if self.flag0==0 or self.flag1==0: return True
        else: return False
        
#v1 = [1, 2]
#v2 = [3, 4, 5, 6]
#a=ZigzagIterator(v1,v2)
#while a.hasNext():
#    print a.next(),

#20. Valid Parentheses 
class Solution(object):
    def isValid(self, s):
        mp={'(':')', '{':'}', '[':']'}
        stack=[]
        for c in s:
            if c in mp: stack.append(c)
            ### remember not stack
            elif not stack or mp[stack.pop()]!=c: return False
        if stack: return False
        return True
        
#a=Solution()
#print a.isValid("()[]{}")
#print a.isValid("([)]")

#66. Plus One
class Solution(object):
    def plusOne(self, digits):
        #res=[]
        res=[0]*len(digits)
        carry=1
        for i in reversed(range(len(digits))):
            cur=carry+digits[i]
            carry=cur/10
            cur=cur%10
            #res.insert(0,cur)
            res[i]=cur # faster
        if carry: res.insert(0,1)
        return res
            
#279. Perfect Squares
class Solution(object):
    def numSquares(self,n): #TLE
        dp=[100]*(n+1)
        dp[0]=0
        dp[1]=1
        for i in range(2,n+1):
            j=1
            while j*j<=n:
                dp[i]=min(dp[i],dp[i-j*j]+1)
                j+=1
        #print dp
        return dp[-1]
        
#a=Solution()
#print a.numSquares(12) #3
#print a.numSquares(13) #2
#print a.numSquares(7691) #3
#print a.numSquares(8829) #2
#print a.numSquares(9975) #4
