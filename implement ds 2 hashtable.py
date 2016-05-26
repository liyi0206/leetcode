class ListNode(object):
    def __init__(self,key,val):
        self.key=key
        self.val=val
        self.next=None

class MyHashTable1(object): ### separate chaining probing (linked list)
    def __init__(self):
        self.N=1<<8               #depends on hashcode algo and memory
        self.heads=[None]*self.N
    
    def set(self,key,val):
        x=hash(key)&(self.N-1)
        if self.heads[x]:
            cur=self.heads[x]
            while cur:
                if cur.key==key: #if key exists, update val
                    cur.val=val
                    return
                cur=cur.next
            
            tmp=self.heads[x]    #if key not exist, add new node to head
            self.heads[x]=ListNode(key,val)
            self.heads[x].next=tmp
        else: self.heads[x]=ListNode(key,val)
    
    def get(self,key):
        x=hash(key)&(self.N-1)
        head=self.heads[x]
        while head:
            if head.key==key: return head.val
            head=head.next
        return None

class MyHashTable2(object): ### linear probing - assuming hashtable big enough
    def __init__(self):     ### assuming space is not full
        self.N=1<<8         #depends on hashcode algo and memory
        self.vals=[None]*self.N
        
    def set(self,key,val):
        x=hash(key)&(self.N-1)
        while self.vals[x] and self.vals[x][0]!=key: x=(x+1)%self.N
        self.vals[x]=(key,val)
        
    def get(self,key):
        x=hash(key)&(self.N-1)
        while self.vals[x] and self.vals[x][0]!=key: x=(x+1)%self.N
        return self.vals[x][1] if self.vals[x] else None
        
a=MyHashTable1()
pairs = [('abc',3),('bce',4),('ddd',5),('afdsfd',6)]
for p in pairs: a.set(p[0],p[1])
print a.get('abc'),a.get('ddd')

a=MyHashTable2()
pairs = [('abc',3),('bce',4),('ddd',5),('afdsfd',6)]
for p in pairs: a.set(p[0],p[1])
print a.get('abc'),a.get('ddd')