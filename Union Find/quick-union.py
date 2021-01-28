class QuickUnion:
    def __init__(self,N):
        self.id = list(range(N))

    def _root(self,i):
        while (self.id[i] != i):
            i = self.id[i]
        return i

    def connected(self,p,q):
        return self._root(p) == self._root(q)

    def union(self,p,q):
        p_root = self._root(p)
        q_root = self._root(q)
        self.id[p_root] = q_root

client = QuickUnion(10)
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