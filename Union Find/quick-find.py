class QuickFind:
    def __init__(self, N):
        self.id = list(range(N))
    
    def connected(self,p,q):
        """Find whelther p and q are in same component"""
        return self.id[p] == self.id[q]
    
    def union(self,p,q):
         """ UNION by changing all entries with id[p] to id[q]."""
        qval = self.id[q]
        pval = self.id[p]

        for index,value in enumerate(self.id):
            if value == pval:
                self.id[index] = qval
        

client = QuickFind(10)
client.union(4,3)
client.union(3,8)
client.union(6,5)
client.union(9,4)
client.union(2,1)
print(client.connected(8,9))
print(client.connected(5,0))
client.union(5,0)
client.union(7,2)
client.union(6,1)

