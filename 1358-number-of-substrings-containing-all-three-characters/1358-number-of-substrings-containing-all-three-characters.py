class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        a = b = c = t = 0
        
        for i, char in enumerate(s, 1):
            if   char == 'a': a = i; t += min(b, c)
            elif char == 'b': b = i; t += min(a, c)
            elif char == 'c': c = i; t += min(a, b)
        
        return t
        