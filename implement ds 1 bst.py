class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.num = 0  ## count of left subtree, including self
        self.next = None
 
#1, insert (and num_smaller,next) - median
#2, delete - hard *****
#3, get kth, get first k (inorder traversal)
#4, get val, closest, closest k, floor, ceiling
#5, based on TreeNode num_smaller 
#   get num_smaller(floor or ceiling) than a val
#   get num_nodes given a range
class BST(object):
    def __init__(self):
        self.root=None
        
    def insert(self,val): #simply add, if equal add to left, no return
        if not self.root: 
            self.root = TreeNode(val) 
            return 0
        cur = self.root
        while cur:
            if val<=cur.val:
                if not cur.left: 
                    cur.left=TreeNode(val)
                    return
                cur=cur.left
            else:
                if not cur.right:
                    cur.right=TreeNode(val)
                    return
                cur=cur.right
         
    def insert1(self,val):  # return the rank of the inserted val 
        if not self.root:   # num_smaller(excluding self)+1
            self.root = TreeNode(val) 
            return 0
        cur = self.root
        num = 0
        while cur:
            if val<=cur.val:
                cur.num+=1
                if not cur.left:
                    cur.left = TreeNode(val)
                    return num
                cur = cur.left
            else:
                num+=cur.num+1
                if not cur.right:
                    cur.right = TreeNode(val)
                    return num
                cur = cur.right
        return num        
     
    def insert2(self,val):  # maintain .next for each node
        if not self.root: 
            self.root = TreeNode(val)
            return
        cur = self.root
        nxt,pre = None,None ###
        while cur:
            if val<=cur.val:
                nxt = cur                       ###
                if cur.left is None:
                    cur.left = TreeNode(val)
                    cur.left.next = nxt         #
                    if pre: pre.next = cur.left #
                    return
                cur = cur.left
            else:
                pre = cur                       ###
                if cur.right is None:
                    cur.right = TreeNode(val)
                    cur.right.next = nxt        #
                    pre.next = cur.right        #
                    return
                cur = cur.right
     
    ### get Kth, inorder
    def inorder(self):
        def dfs(node):
            if not node: return
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)
        res = []
        dfs(self.root)
        return res
     
    def getKth(self,K): #if no Kth (k>n), return None
        cur = self.root
        while cur:
            if cur.num<K:
                K-=cur.num+1 ###
                cur=cur.right
            elif cur.num>K:
                cur=cur.left
            else: return cur
            
    ### val, floor, ceiling, closest
    def getVal(self,val): #if val not exist, return None
        cur=self.root
        while cur:
            if cur.val==val: return cur
            elif cur.val<val:
                cur=cur.right
            else: cur=cur.left
    def getFloor(self,val): #if no val, return floor; if val, return self
        pass
    def getCeiling(self,val):
        pass
    def getClosest(self,val):
        pass
    def getClosestK(self,val):
        pass
        
    ### based on num_smaller
    def getNumSmaller1(self,val): #floor
        pass
    def getNumSmaller2(self,val): #ceiling
        pass
    def getNumBetween(self,val1,val2):
        pass

    ### delete
    def getMin(self,node): # input root node, return min node
        if not node: return None
        while node.left: node=node.left
        return node
    def deMin(self,node): # input root node, return new root node
        if not node: return None
        if node.left: 
            node.left = self.deMin(node.left) # recursion
            return node 
        else: 
            return node.right # if node.right, that's it; if not, return None
        
    def delete(self,val):
        self.root=self.rec(self.root,val)

    def rec(self,cur,val): #recur only for delete
        if not cur: return None
        
        if val<cur.val: cur.left = self.rec(cur.left,val)
        elif val>cur.val: cur.right = self.rec(cur.right,val)
        else:
            if not cur.left: return cur.right # no matter cur.right or not
            if not cur.right: return cur.left 
            # if have both children, get right min, that will be the new node
            # when cur node is deleted. 
            tmp = cur
            cur = self.getMin(tmp.right)     ### a new cur, which is right min
            cur.left = tmp.left              # cur.left is the old left
            cur.right= self.deMin(tmp.right) # cur.right is the old right, except for deMin
                                             # root might change, in the case only one node
                                             # return None
        return cur

class BST_tmp(object):
    def __init__(self):
        self.root=None
        
    def insert(self,val): # no dup val
        if not self.root: 
            self.root=TreeNode(val)
            return 
        cur=self.root
        while cur:
            if val<cur.val: 
                if cur.left: cur=cur.left
                else: 
                    cur.left =TreeNode(val)
                    break
            elif val>cur.val: 
                if cur.right: cur=cur.right
                else: 
                    cur.right=TreeNode(val)
                    break
        
    def delete(self,val):
        prev=None
        cur=self.root
        while cur:
            if val==cur.val:
                if not cur.left: 
                    if not prev: self.root=cur.right
                    elif prev.val>cur.val: prev.left=cur.right
                    else: prev.right=cur.right
                    return
                elif not cur.right:
                    if not prev: self.root=cur.left
                    elif prev.val>cur.val: prev.left=cur.left
                    else: prev.right=cur.left
                    return
                else:
                    if not cur.right.left: 
                        cur.right.left=cur.left
                        cur.right.right=None
                        #print "cur.right.left.val",cur.right.left.val
                        if not prev: return cur.right#
                        if prev.val>cur.val: prev.left=cur.right; break#
                        else: prev.right=cur.right; break#
                    else:
                        tmp=cur.right
                        while tmp.left.left: tmp=tmp.left 
                        rightmin=tmp.left
                        
                        if not tmp.left.right: tmp.left=None
                        else: tmp.left=tmp.left.right
                        
                        rightmin.left=cur.left
                        rightmin.right=cur.right
                        cur=rightmin
                    
            elif val<cur.val: 
                prev=cur
                cur=cur.left
            else:
                prev=cur
                cur=cur.right
            

tree=BST()
tree.insert(5)
tree.insert(2)
tree.insert(4)
tree.insert(3)
tree.insert(1)
tree.delete(2)

print tree.root.val
print tree.root.left.val
print tree.root.left.left.val
print tree.root.left.right.val
print 

tree=BST()
tree.insert(5)
tree.insert(2)
tree.insert(3)
tree.insert(1)
tree.delete(2)

print tree.root.val
print tree.root.left.val
print tree.root.left.left.val
print

tree=BST()
tree.insert(5)
tree.insert(2)
tree.insert(3)
tree.delete(5)

print tree.root.val
print tree.root.right.val
print

tree=BST()
tree.insert(5)
tree.insert(2)
tree.insert(3)
tree.delete(2)

print tree.root.val
print tree.root.left.val
print tree.root.left.right