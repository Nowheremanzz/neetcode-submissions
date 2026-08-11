class TimeMap:

    def __init__(self):
        self.dict = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dict[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res_li = self.dict[key]
        l = 0
        r = len(res_li)
        while l < r:
            m = l + (r - l) // 2
            if res_li[m][1] <= timestamp:
                l = m + 1
            else:
                r = m
        return res_li[r - 1][0] if r > 0 else ""
