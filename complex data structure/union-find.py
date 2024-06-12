# 并查集
class UF:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
    
    def find(self, p):
        while p != self.parent[p]:
            p = self.parent[p]
        return p

    def union(self, p, q):
        self.parent[self.find(p)] = self.find(q)
