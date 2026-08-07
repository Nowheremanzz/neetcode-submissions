class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        middle = len(nums) // 2
        if nums[middle] == target:
            return middle
        elif nums[middle] > target:
            return self.search(nums[:middle], target)
        elif nums[middle] < target:
            result = self.search(nums[middle+1:], target)
            if result == -1:
                return -1
            else:
                return middle + 1 + result