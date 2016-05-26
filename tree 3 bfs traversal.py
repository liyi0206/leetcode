


#102 level order traversal
class Solution(object):
    def levelOrder(self,root):
        if not root: return []
        res=[]
        cur=[root]
        while cur:
            tmp=[]
            next=[]
            for c in cur:
                tmp.append(c.val)
                if c.left: next.append(c.left)
                if c.right:next.append(c.right)
            res.append(tmp)
            cur=next
        return res
                
root=TreeNode(3)
root.left =TreeNode(9)
root.right=TreeNode(20)
root.right.left =TreeNode(15)
root.right.right=TreeNode(7)

a=Solution()
print a.levelOrder(root)