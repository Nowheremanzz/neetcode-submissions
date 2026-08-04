class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = ""
        l = 0
        count_t = defaultdict(int)
        count_s = defaultdict(int)
        for c in t:
            count_t[c] += 1
        for r in range(len(s)):
            count_s[s[r]] += 1
            if (all(count_s[c] >= count_t[c] for c in count_t)):
                while count_s[s[l]] > count_t[s[l]]:
                    count_s[s[l]] -= 1
                    l += 1
                candi = s[l:r+1]
                if not res:
                    res = candi
                else:
                    if len(candi) < len(res):
                        res = candi
        return res
            
        