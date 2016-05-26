#146. LRU Cache
# for set, another possibility is to update!
class LRUCache(object):
    def __init__(self,capacity):
        self.capacity=capacity
        self.cache={}
        self.queue=[]
        
    def get(self,key):
        if key in self.cache: 
            self.queue.remove(key)
            self.queue.append(key)
            return self.cache[key]
        else: return -1
    
    def set(self,key,value):
        if key not in self.cache:
            if len(self.cache)==self.capacity:
                tmp=self.queue.pop(0)
                self.cache.pop(tmp,None)
            self.cache[key]=value
            self.queue.append(key)
        else:
            self.cache[key]=value
            self.queue.remove(key)
            self.queue.append(key)
   
#a=LRUCache(2)
#print a.get(2)
#a.set(2,6)
#print a.get(1)
#a.set(1,5)
#a.set(1,2)
#print a.get(1)
#print a.get(2)

#a=LRUCache(2)
#a.set(2,1)
#a.set(1,1)
#a.set(2,3)
#a.set(4,1)
#print a.get(1)
#print a.get(2)

#155. Min Stack
# don't forget to add "if self.minStack==[] or"
class MinStack(object):
    def __init__(self):
        self.stack=[]
        self.minStack=[]
        
    def push(self,x):
        self.stack.append(x)
        if self.minStack==[] or x<=self.minStack[-1]:
            self.minStack.append(x)
        
    def pop(self):
        if self.stack: 
            tmp=self.stack.pop()
            if tmp==self.minStack[-1]: self.minStack.pop()
        
    def top(self):
        return self.stack[-1] if self.stack else None
        
    def getMin(self):
        return self.minStack[-1]

a=MinStack()
a.push()

#208. Implement Trie (Prefix Tree)
# need a TrieNode
# need to initialize Trie with self.root=TrieNode()
# remember to make cur=cur.children[c] 
class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children = dict()
        self.isWord = False
        
class Trie(object):
    def __init__(self):
        self.root=TrieNode()
        
    def insert(self,word):
        cur=self.root
        for c in word:
            if c not in cur.children:
                cur.children[c]=TrieNode()
            cur=cur.children[c] 
        cur.isWord=True
        
    def search(self,word): #return True/False
        cur=self.root
        for c in word:
            if c not in cur.children: return False
            cur=cur.children[c]
        return cur.isWord
        
    def startsWith(self,prefix): #return True/False
        cur=self.root
        for c in prefix:
            if c not in cur.children: return False
            cur=cur.children[c]
        return True

#225. Implement Stack using Queues
# when push, only put at end, don't pop until top
# because when push more, the sequence will be wrong
# when pop or peak, iterate everything

#232. Implement Queue using Stacks
# reuse self.peek()
# empty() return not self.stack and not self.tmp
class Queue(object):
    def __init__(self):
        self.stack=[]
        self.tmp=[]
        
    def push(self,x):
        self.stack.append(x)
        
    def pop(self): #return nothing
        self.peek()
        self.tmp.pop()
        
    def peek(self):
        if not self.stack and not self.tmp: return None
        if not self.tmp: 
            while self.stack:
                a=self.stack.pop()
                self.tmp.append(a)
        return self.tmp[-1]
    
    def empty(self):
        return not self.stack and not self.tmp