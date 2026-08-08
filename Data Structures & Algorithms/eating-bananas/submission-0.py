class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_pile = max(piles)
        l, r = 1, max_pile + 1
        while l < r:
            k = l + (r - l) // 2
            needed = 0
            for p in piles:
                needed += -(-p // k)
            if needed > h:
                l = k + 1
            elif needed <= h:
                r = k
        return l