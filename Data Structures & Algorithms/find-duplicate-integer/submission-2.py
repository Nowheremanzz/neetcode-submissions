class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = nums[0]
        while n != nums[n]:
            temp = nums[n]
            nums[n] = n
            n = temp
        return n