#146 LRU Cache
### for each (key,val), 
#save key as hashmap key, also we need value as ListNode for hashmap
#save kay as linked list key (for linking back to hashmap when delete tail),  
#save val as linked list val, also we need pre and post for linked list

class DLNode(object):
    def __init__(self,key,val):
        self.key=key
        self.val=val
        self.pre=None
        self.nxt=None
        
class LRUCache(object):
    def __init__(self,capacity):
        self.cap=capacity
        self.mp={}
        self.head=DLNode(0,0)
        self.tail=DLNode(0,0)
        self.head.nxt=self.tail
        self.tail.pre=self.head
        
    def rmNode(self,node):
        pre,nxt=node.pre,node.nxt
        pre.nxt,nxt.pre=nxt,pre
        
    def addTail(self,node):
        pre=self.tail.pre
        pre.nxt,node.pre=node,pre
        node.nxt,self.tail.pre=self.tail,node
        
    def get(self,key):
        if key in self.mp:
            node=self.mp[key]
            self.rmNode(node)
            self.addTail(node)
            return node.val
        else: return -1
        
    def set(self,key,val):
        new_node=DLNode(key,val)
        if key in self.mp:
            node=self.mp[key]
            self.rmNode(node)
            self.addTail(new_node)
            self.mp[key]=new_node
        else:
            if len(self.mp)==self.cap:
                tmp=self.head.nxt
                self.rmNode(tmp)
                self.mp.pop(tmp.key) ##
            self.addTail(new_node)
            self.mp[key]=new_node
            
print "case1"   
a=LRUCache(1)
a.set(2,1)
print a.get(2) #1

print "case2"
a=LRUCache(1)
a.set(2,1)
print a.get(2) #1
a.set(3,2)
print a.get(2) #None
print a.get(3) #2

print "case3"
a=LRUCache(2)
print a.get(2)
a.set(2,6)
print a.get(1)
a.set(1,5)
a.set(1,2)
print a.get(1)
print a.get(2)