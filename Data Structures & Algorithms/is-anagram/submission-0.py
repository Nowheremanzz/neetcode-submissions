class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic_s = {}
        for char in s:
            if char in dic_s:
                dic_s[char] += 1
            else:
                dic_s[char] = 1
        dic_t = {}
        for char in t:
            if char in dic_t:
                dic_t[char] += 1
            else:
                dic_t[char] = 1
        if len(dic_s.keys()) != len(dic_t.keys()):
            return False
        for key in dic_s:
            if key not in dic_t:
                return False
            if dic_s[key] != dic_t[key]:
                return False
        return True