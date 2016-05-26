# I, undirected graph
#133. Clone Graph
#138. Copy List with Random Pointer

# II, undirected graph - union find
#261. Graph Valid Tree (*) - tree related
#305. Number of Islands II - not really graph
#323. Number of Connected Components in an Undirected Graph

# III, directed graph - topological sort (BFS)
#310. Minimum Height Trees (*) - tree related

#207. Course Schedule
#210. Course Schedule II
#269. Alien Dictionary
class Solution(object):
    def alienOrder(self, words):
        #if not words: return ""
        if len(set(words))==1: return words[0]
        st=set()
        for word in words:
            for c in word: st.add(c) 
        #print st
        mp ={x:set() for x in st}
        mp2={x:set() for x in st}
        for i in range(len(words)-1):
            j=0
            while words[i+1][j]==words[i][j] and \
                  j<min(len(words[i]),len(words[i+1]))-1: j+=1
            mp[words[i+1][j]].add(words[i][j])
            mp2[words[i][j]].add(words[i+1][j])
        #print mp
        #print mp2
        
        cur=[x for x in mp if not mp[x]]#;print cur
        res=""
        while cur and st:
            res+="".join(cur)#; print res
            for x in cur: st.remove(x)
            nxt=[]
            for x in cur:
                for y in mp2[x]:
                    mp[y].remove(x)
                    if not mp[y]: nxt.append(y)
            cur=nxt#; print cur
        return res if not st else ""

a=Solution()
print a.alienOrder(["wrt","wrf","er","ett","rftt"]) #"wertf"
print a.alienOrder(["za","zb","ca","cb"]) #zcab
print a.alienOrder([])
print a.alienOrder(["z","z"]) #z