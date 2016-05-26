class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#I, Basics - traversal - recur and iter (*), return list
#94. Binary Tree Inorder Traversal - ** if BST, asc sorted list
class Solution(object):
    def inorderTraversal(self,root):
        self.res=[]
        self.dfs(root)
        return self.res
        
    def dfs(self,node):
        if not node: return
        self.dfs(node.left)
        self.res.append(node.val)
        self.dfs(node.right)
        
class SolutionIter(object):
    def inorderTraversal(self,root):
        res=[]
        cur,stack=root,[]
        while cur or stack:
            if cur:
                stack.append(cur)
                cur=cur.left
            else: 
                parent=stack.pop()
                res.append(parent.val)
                cur=parent.right
        return res

#root=TreeNode(2)
#root.left =TreeNode(1)
#root.right=TreeNode(3)
#a=Solution()
#print a.inorderTraversal(root)

#144. Binary Tree Preorder Traversal - root first
class SolutionIter(object):
    def preorderTraversal(self,root):
        res=[]
        cur,stack=root,[]
        while cur or stack:
            if cur:
                res.append(cur.val)
                if cur.right: stack.append(cur.right)
                cur=cur.left
            else: cur=stack.pop()
        return res
        
#145. Binary Tree Postorder Traversal (**) - root last
class SolutionIter(object):
    def postorderTraversal(self, root):
        res,stack=[],[] 
        cur,prev=root,None
        while cur or stack:
            if cur:
                stack.append(cur)
                cur=cur.left
            else:
                parent = stack[-1]
                if parent.right in (None, prev):
                    prev=stack.pop()
                    res.append(prev.val)
                else:
                    cur=parent.right
        return res
        
#230. Kth Smallest Element in a BST (*) - extension of inorder traversal
#if recur, need global flag for found. or iter, more efficient.
class Solution(object):
    def kthSmallest(self,root,k):
        self.k=k
        self.res=[]
        self.dfs(root)
        return self.res[-1]
    def dfs(self,node):
        if not node: return
        self.dfs(node.left)
        if len(self.res)<self.k:
            self.res.append(node.val)
        self.dfs(node.right)

#root=TreeNode(2)
#root.left =TreeNode(1)
#root.right=TreeNode(4)
#root.right.left =TreeNode(3)
#root.right.right=TreeNode(5)
#      
#a=Solution()
#print a.kthSmallest(root,3)

#II, convert(*)
#105. Construct Binary Tree from Preorder and Inorder Traversal - dfs, find root
class Solution(object):
    def buildTree(self, preorder, inorder): #MLE ???
        if not inorder or not preorder: return None
        for i in range(len(inorder)):
            if inorder[i]==preorder[0]:break
        root=TreeNode(inorder[i])
        root.left =self.buildTree(preorder[1:i+1],inorder[:i])
        root.right=self.buildTree(preorder[i+1:],inorder[i+1:])
        return root
        
    def buildTree2(self, preorder, inorder):
        if not inorder or not preorder: return None
        for i in range(len(inorder)):
            if inorder[i]==preorder[0]:break
        root=TreeNode(preorder.pop(0))
        root.left =self.buildTree(preorder,inorder[:i])
        root.right=self.buildTree(preorder,inorder[i+1:])
        return root

a=Solution()
new = a.buildTree([3,2,1,4,5],[1,2,3,4,5])
print new.val
print new.left.val
print new.left.left.val
print new.right.val
print new.right.right.val

#106. Construct Binary Tree from Inorder and Postorder Traversal - dfs, find root
#108. Convert Sorted Array to Binary Search Tree - asc array -> height balanced bst
class Solution(object):
    def sortedArrayToBST(self, nums):
        if not nums: return None
        mid = len(nums)/2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right =self.sortedArrayToBST(nums[mid+1:])
        return root
        
#109. Convert Sorted List to Binary Search Tree (**)
#asc linked list -> height balanced bst - preorder traverse
# *** self.cur ***
class Solution(object):
    def sortedListToBST(self, head):
        n,cur=0,head
        while cur:
            n+=1
            cur=cur.next
        self.cur=head
        return self.dfs(n)
    
    def dfs(self,L):
        if L<=0: return None
        
        left = self.dfs(L/2)
        root = TreeNode(self.cur.val) #*
        self.cur = self.cur.next

        root.left = left
        root.right= self.dfs(L-L/2-1)
        return root

#114. Flatten Binary Tree to Linked List (*) - in place
# *** self.last ***
class Solution(object):
    last = None
    def flatten(self, root):
        if not root: return None
        self.flatten(root.right)
        self.flatten(root.left)
        root.right=self.last #*
        root.left =None
        self.last =root
        
#III, LCA (*)
#235. Lowest Common Ancestor of a Binary Search Tree
#236. Lowest Common Ancestor of a Binary Tree (**)
class Solution(object): #BST
    def lowestCommonAncestor(self, root, p, q):
        cur=root
        while cur:
            if p.val<cur.val and q.val<cur.val:
                cur=cur.left
            elif p.val>cur.val and q.val>cur.val:
                cur=cur.right
            else: return cur
            
class Solution2(object): #BT
    def lowestCommonAncestor(self, root, p, q):
        if not root or root.val==p or root.val==q: 
            return root
        left =self.lowestCommonAncestor(root.left, p,q)
        right=self.lowestCommonAncestor(root.right,p,q)
        if not left: return right
        elif not right: return left
        else: return root
        

#IV, Hard
#99. Recover Binary Search Tree (**) - inorder traverse