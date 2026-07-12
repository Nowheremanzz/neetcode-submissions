class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_n = defaultdict(int)
        for num in nums:
            dict_n[num] += 1
        freq = [[] for _ in range(len(nums) + 1)] 
        for key, value in dict_n.items():
            freq[value].append(key)
        result = []
        for i in range(len(freq) - 1, -1, -1):
            if k == 0:
                break
            if freq[i]:
                result += freq[i]
                k -= len(freq[i])
        return result