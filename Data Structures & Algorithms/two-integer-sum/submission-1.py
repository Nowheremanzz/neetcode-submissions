class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = sorted(nums)
        i = 0
        j = len(nums) - 1
        while(i < j):
            if sorted_nums[i] + sorted_nums[j] == target:
                break
            if sorted_nums[i] + sorted_nums[j] > target:
                j -= 1
            if sorted_nums[i] + sorted_nums[j] < target:
                i += 1
        result = []
        for n, num in enumerate(nums):
            if num == sorted_nums[i] or num == sorted_nums[j]:
                result.append(n)
        return result