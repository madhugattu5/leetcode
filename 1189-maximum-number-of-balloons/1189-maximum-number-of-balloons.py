class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloon = set({'b', 'a', 'l', 'o', 'n'})
        d = {}
        for i in text:
            if i in balloon:
                if i in d:
                    d[i] += 1
                else:
                    d[i] = 1
        return min(
                    d.get('b', 0),
                    d.get('a', 0),
                    d.get('l', 0) // 2,
                    d.get('o', 0) // 2,
                    d.get('n', 0)
                )