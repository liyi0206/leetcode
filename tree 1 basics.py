class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#I, Basics - not consider structure
#98. Validate Binary Search Tree (*)
# if root is none, return True
class Solution(object):
    def isValidBST(self,root):
        return self.dfs(root,1000000,-1000000)
        
    def dfs(self,node,upper,lower):
        if not node: return True
        if not (lower<node.val<upper): return False
        return self.dfs(node.left, node.val,lower) and \
               self.dfs(node.right,upper,node.val)

#root=TreeNode(10)
#root.left=TreeNode(5)
#root.right=TreeNode(15)
#root.right.left =TreeNode(6)
#root.right.right=TreeNode(20)

#a=Solution()
#print a.isValidBST(root) #F
        
#100. Same Tree
class Solution(object):
    def isSameTree(self,p,q):
        if not p and not q: return True
        elif not p or not q: return False
        elif p.val!=q.val: return False
        else: 
            return self.isSameTree(p.left, q.left) and \
                   self.isSameTree(p.right,q.right)
        
#101. Symmetric Tree
# need extra dfs for (left,right)
# don't forget elif left.val!=right.val: return False
class Solution(object):
    def isSymmetric(self,root):
        if not root: return True
        return self.dfs(root.left, root.right)
            
    def dfs(self,left,right):
        if not left and not right: return True
        elif not left or not right:return False
        elif left.val!=right.val: return False
        else: 
            return self.dfs(left.left, right.right) and \
                   self.dfs(left.right,right.left)

#226. Invert Binary Tree
class Solution(object):
    def invertTree(self,root):
        if not root: return
        root.right,root.left=self.invertTree(root.left),self.invertTree(root.right)
        return root

#II, Basics - not to leaf nodes
# 110 balanced bt (*) 
# definition 1 leetcode version
# need 2 params, one for <1 true/false, one for depth
class Solution1(object):
    def isBalanced(self,root): #TLE
        self.res=True
        maxdp=self.dfs(root)
        return self.res
        
    def dfs(self,node):
        if not node: return 0
        if not node.left and not node.right: return 1
        elif not node.left: dp=self.dfs(node.right)+1
        elif not node.right:dp=self.dfs(node.left)+1
        else: 
            dp1=self.dfs(node.left)
            dp2=self.dfs(node.right)
            if abs(dp1-dp2)>1: 
                self.res=False
            dp=max(self.dfs(node.left), self.dfs(node.right))+1
        return dp
        
# combine True/False into dp, so to prune earlier (*)
class Solution12(object):
    def isBalanced(self,root):
        return self.dfs(root)!=-1
        
    def dfs(self,node):
        if not node: return 0
        h1=self.dfs(node.left)
        if h1==-1: return -1
        h2=self.dfs(node.right)
        if h2==-1 or abs(h1-h2)>1: return -1
        return max(h1,h2)+1

root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(2)
root.left.left=TreeNode(3)
root.left.right=TreeNode(3)
root.right.left=TreeNode(3)
root.right.left.left=TreeNode(4)

#a=Solution1()
#print a.isBalanced(root)

# definition 2 cracking code version
# need two properties - depth min/max
# and compare diff max/min to determine
class Solution2(object):
    def isBalanced(self,root):
        if not root: return None
        self.min,self.max=100000,-1
        return self.dfs(root,0)
        
    def dfs(self,node,depth):
        if not node: 
            self.min=min(self.min,depth)
            self.max=max(self.max,depth)
            if self.max-self.min>1: return False
            else: return True
        return self.dfs(node.left, depth+1) and \
               self.dfs(node.right,depth+1)

class Solution22(object):
    def isBalanced(self,root):
        if not root: return None
        self.min,self.max=100000,-1
        self.dfs(root,0)
        return False if self.max-self.min>1 else True
        
    def dfs(self,node,depth):
        if not node: 
            self.min=min(self.min,depth)
            self.max=max(self.max,depth)
            return
        self.dfs(node.left, depth+1)
        self.dfs(node.right,depth+1)

#a=Solution22()
#print a.isBalanced(root) #w/ 4, F, w/o 4 True

#104. Maximum Depth of Binary Tree
class Solution(object):
    def maxDepth(self,root):
        self.res=0
        self.dfs(root,0)
        return self.res
        
    def dfs(self,node,dp):
        if not node:
            self.res=max(self.res,dp)
            return
        self.dfs(node.left, dp+1)
        self.dfs(node.right,dp+1)

#124. Binary Tree Maximum Path Sum (*)
class Solution(object):
    def maxPathSum(self,root):
        if not root: return None
        self.res=-1000000
        self.dfs(root)
        return self.res
        
    def dfs(self,node):
        if not node.left and not node.right: 
            self.res=max(self.res,node.val)
            return node.val
        left =self.dfs(node.left) if node.left else 0
        right=self.dfs(node.right) if node.right else 0
        tmp=max(node.val,
                left+node.val,
                right+node.val,
                left+right+node.val)
        self.res=max(self.res,tmp)
        return max(node.val,left+node.val,right+node.val)
        
class BetterSolution(object):
    def maxPathSum(self,root):
        self.res=-1000000
        self.dfs(root)
        return self.res
        
    def dfs(self,root):
        if root is None: return 0
        left = self.dfs(root.left)
        right= self.dfs(root.right)
        tmp=max(root.val,
                left+root.val, 
                right+root.val, 
                left+right+root.val)
        self.res = max(self.res,tmp)
        return max(left+root.val, right+root.val, root.val)
        
root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(3)
a=Solution()
print a.maxPathSum(root)

#298. Binary Tree Longest Consecutive Sequence 
# increasing sequence, return length
# From parent to child (not reverse)
# From any parent to any child (not only root and leaf)
class Solution(object):
    def longestConsecutive(self, root):
        self.res=0
        self.dfs(root,None,0) #keep cur and prev, count. no return
        return self.res
        
    def dfs(self,node,prev,num):
        if not node: 
            self.res=max(self.res,num)
            return
        if not prev or prev.val+1==node.val: 
            self.dfs(node.left,node,num+1)
            self.dfs(node.right,node,num+1)
        else:
            self.res=max(self.res,num)
            self.dfs(node.left,node,1) # 1 represents parent
            self.dfs(node.right,node,1)

#III, Basics - must to leaf nodes
#111. Minimum Depth of Binary Tree
# need to determine on if not node.left and not node.right
class Solution(object):
    def minDepth(self,root):
        if not root: return 0
        self.res=1000000
        self.dfs(root,1)
        return self.res
        
    def dfs(self,node,dp):
        if not node.left and not node.right:
            self.res=min(self.res,dp)
            return
        if node.left: self.dfs(node.left, dp+1)
        if node.right:self.dfs(node.right,dp+1)
   
#root=TreeNode(1)
#root.left=TreeNode(2)
#root.right=TreeNode(2)
#root.left.left=TreeNode(3)
#root.left.right=TreeNode(3)
#root.right.left=TreeNode(3)
#root.right.left.left=TreeNode(4)
#
#a=Solution()
#print a.minDepth(root)
     
#112. Path Sum
# if no more node then return, sub if tmp==val then update res
# leaf node - if not node.left and not node.right
class Solution(object):
    def hasPathSum(self,root,sum):
        if not root: return False
        self.res=False
        self.dfs(root,sum-root.val)
        return self.res

    def dfs(self,node,tmp):
        if not node.left and not node.right:
            if tmp==0: self.res=True
            return
        if node.left: self.dfs(node.left, tmp-node.left.val)
        if node.right:self.dfs(node.right,tmp-node.right.val)

root=TreeNode(5)
root.left=TreeNode(4)
root.right=TreeNode(8)
root.left.left=TreeNode(11)
root.right.left=TreeNode(13)
root.right.right=TreeNode(4)
root.left.left.left=TreeNode(7)
root.left.left.right=TreeNode(2)
root.right.right.right=TreeNode(1)

#a=Solution()
#print a.hasPathSum(root, 22)

#113. Path Sum II
class Solution(object):
    def pathSum(self,root,sum):
        if not root: return []
        self.sum=sum
        self.res=[]
        self.dfs(root,[root.val])
        return self.res
        
    def dfs(self,node,path):
        if not node.left and not node.right:
            if sum(path)==self.sum: self.res.append(path)
        if node.left: self.dfs(node.left, path+[node.left.val])
        if node.right:self.dfs(node.right,path+[node.right.val])


root=TreeNode(5)
root.left=TreeNode(4)
root.right=TreeNode(8)
root.left.left=TreeNode(11)
root.right.left=TreeNode(13)
root.right.right=TreeNode(4)
root.left.left.left=TreeNode(7)
root.left.left.right=TreeNode(2)
root.right.right.left=TreeNode(5)
root.right.right.right=TreeNode(1)

#a=Solution()
#print a.pathSum(root,22)

#129. Sum Root to Leaf Numbers
# Find the total sum of all root-to-leaf numbers
class Solution(object):
    def sumNumbers(self, root):
        if root==None: return 0
        self.res=0
        self.dfs(root, 0)
        return self.res

    def dfs(self, root, sum):
        if not root.left and not root.right:
            self.res += 10*sum+root.val
        if root.left: self.dfs(root.left, 10*sum+root.val)
        if root.right:self.dfs(root.right,10*sum+root.val)

#257. Binary Tree Paths
# return all root-to-leaf paths
class Solution(object):
    def binaryTreePaths(self, root):
        if not root: return []
        self.res=[]
        self.dfs(root,[])
        return self.res
        
    def dfs(self,root,path):
        if not root.left and not root.right:
            self.res.append("->".join(path+[str(root.val)]))
        if root.right:self.dfs(root.right,path+[str(root.val)])
        if root.left: self.dfs(root.left, path+[str(root.val)])