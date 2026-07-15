class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_side, right_side = [], []
        prod = 1
        for n in nums:
            prod = prod * n
            left_side.append(prod)
        prod = 1
        for i in range(len(nums)-1, -1, -1):
            prod = prod * nums[i]
            right_side.append(prod)
        res = []
        for i in range(len(nums)):
            if i-1 < 0:
                res.append(right_side[len(nums)-2-i])
            elif i+1 >= len(nums):
                res.append(left_side[i-1])
            else:
                res.append(left_side[i-1] * right_side[len(nums)-2-i])
        return res