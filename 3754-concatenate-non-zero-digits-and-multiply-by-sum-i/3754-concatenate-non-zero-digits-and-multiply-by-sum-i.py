class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x, sum, tens=0, 0, 1
        while n:
            n, d=divmod(n, 10)
            sum+=d
            if d:
                x+=tens*d
                tens*=10
        return x*sum
        