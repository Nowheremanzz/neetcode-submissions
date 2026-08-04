class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter = defaultdict(int)
        for s in s1:
            counter[s] -= 1
        l_s, l, r = len(s1), 0, 0
        if len(s1) > len(s2):
            return False
        for r in range(l_s):
            counter[s2[r]] += 1
        while r < len(s2):
            if all(c == 0 for c in counter.values()):
                return True
            counter[s2[l]] -= 1
            l += 1
            r += 1
            if r < len(s2):
                counter[s2[r]] += 1
        return False