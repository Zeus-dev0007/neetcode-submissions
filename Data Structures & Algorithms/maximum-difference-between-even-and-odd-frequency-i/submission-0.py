class Solution:
    def maxDifference(self, s: str) -> int:
        counts = Counter(s).values()

        odds = []
        evens = []

        for f in counts:
            if f % 2 == 1:
                odds.append(f)

            else:
                evens.append(f)

        return max(odds) - min(evens)