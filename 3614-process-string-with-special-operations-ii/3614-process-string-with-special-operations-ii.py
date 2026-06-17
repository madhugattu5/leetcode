class Solution:
    def processStr(self, s: str, k: int) -> str:
        L = 0
        for char in s:
            if 'a' <= char <= 'z': L += 1
            elif char == '*': L = max(0, L - 1)
            elif char == '#': L *= 2
       
        if k < 0 or k >= L: 
            return '.'
        rev = False
        for char in reversed(s):
            if char == '%':
                rev = not rev
                k = (L - 1 - k)
            elif char == '#':
               
                L //= 2
                if k >= L: k -= L
            elif char == '*':
               
                L += 1
            elif 'a' <= char <= 'z':
                
                if k == (L - 1): 
                    return char
                L -= 1
        
        return '.'