# 树状数组（将前缀区间二进制分解成关键区间）
# O(log n) 单点修改，区间查询
# https://leetcode.cn/problems/range-sum-query-mutable/solutions/2524481/dai-ni-fa-ming-shu-zhuang-shu-zu-fu-shu-lyfll
class Fenwick:
    __slots__ = 'f'

    def __init__(self, n: int): # 这里的n是数据数组的长度+1（因为树状数组的位置0没用到）
        self.f = [0] * n

    def update(self, i: int, val: int) -> None:
        while i < len(self.f):
            self.f[i] += val
            i += i & -i

    def pre(self, i: int) -> int:
        res = 0
        while i > 0:
            res += self.f[i]
            i &= i - 1
        return res

    def query(self, l: int, r: int) -> int:
        return self.pre(r) - self.pre(l - 1)
