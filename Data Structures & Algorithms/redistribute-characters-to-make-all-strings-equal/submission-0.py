class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        res = ""
        for i in words:
            res += i

        count = Counter(res)

        for c in count.values():
            if c % len(words) != 0:
                return False
        
        return True
        