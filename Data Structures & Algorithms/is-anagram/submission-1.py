class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s = [0] * 26
        for char in s:
            count_s[ord(char) - ord('a')] += 1
        count_t = [0] * 26
        for char in t:
            count_t[ord(char) - ord('a')] += 1
        for i in range(26):
            if count_s[i] != count_t[i]:
                return False
        return True