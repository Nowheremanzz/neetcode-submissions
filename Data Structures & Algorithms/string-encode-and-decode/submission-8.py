class Solution:

    def encode(self, strs: List[str]) -> str:
        builder = []
        for string in strs:
            builder.append(str(len(string)) + "#")
            builder.append(string)
        res = "".join(builder)
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        j = 1
        while j < len(s):
            if s[j] == "#":
                length = int(s[i:j])
                string = s[j+1:j+length+1]
                res.append(string)
                i = j+length+1
                j = i + 1
            else:
                j += 1
        return res