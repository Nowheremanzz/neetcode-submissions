class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs:
            return "-".join(strs)
        else:
            return "empty list"

    def decode(self, s: str) -> List[str]:
        if s != "empty list":
            return s.split("-")
        else:
            return []