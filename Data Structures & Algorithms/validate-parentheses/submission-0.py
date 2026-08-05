class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        p_dict = {")": "(", "}": "{", "]": "["}
        for p in s:
            if p in p_dict.values():
                stack.append(p)
            if p in p_dict:
                if not stack:
                    return False
                else:
                    if stack[-1] != p_dict[p]:
                        return False
                    else:
                        stack.pop()
        if not stack:
            return True
        else:
            return False