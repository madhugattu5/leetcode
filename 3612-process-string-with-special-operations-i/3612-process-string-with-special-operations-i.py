class Solution:
    def processStr(self, s: str) -> str:
        result = []

        for ch in s:
            if ch.isalpha():  
                result.append(ch)
            elif ch == '*':
                if result:
                    result.pop()
            elif ch == '#':
                result = result + result
            elif ch == '%':
                result.reverse()

        return "".join(result)