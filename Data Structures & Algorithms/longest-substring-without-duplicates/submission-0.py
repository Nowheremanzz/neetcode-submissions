class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        check = defaultdict(int)
        l, r = 0, 0
        maximum = 0
        length = 0
        while r < len(s):
            if not check[s[r]]:
                check[s[r]] += 1
                length += 1
                r += 1
            else:
                while check[s[r]]:
                    check[s[l]] -= 1
                    length -= 1
                    l += 1
            maximum = max(maximum, length)
        return maximum