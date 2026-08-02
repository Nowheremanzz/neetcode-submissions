class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        count = defaultdict(int)
        length = 0
        max_count = 0
        for r in range(len(s)):
            count[s[r]] += 1
            max_count = max(max_count, count[s[r]])
            if r - l + 1 - max_count <= k:
                length = max(length, r - l + 1)
            else:
                count[s[l]] -= 1
                l += 1
        return length