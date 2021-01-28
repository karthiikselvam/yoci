class WeightedUnion:
    def __init__(self,N):
        self.id = list(range(N))
        self.size = [1] * N
    
    def _root(self,i):
        while (self.id[i] != i):
            i = self.id[i]
        
        return i

    def connected(self,p,q):
        p_val = self._root(p)
        q_val = self._root(q)
        return p_val == q_val

    def union(self,p,q):
        p_root = self._root(p)
        q_root = self._root(q)

        if self.size[p_root] < self.size[q_root]:
            self.id[p_root] = q_root
            self.size[q_root] += self.size[p_root]
        else :
            self.id[q_root] = p_root
            self.size[p_root] += self.size[q_root]

client = WeightedUnion(10)
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