class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_n = defaultdict(int)
        for num in nums:
            dict_n[num] += 1
        sorted_l = sorted(dict_n.items(), key = lambda item: item[1], reverse = True)
        result = []
        for i in range(k):
            result.append(sorted_l[i][0])
        return result