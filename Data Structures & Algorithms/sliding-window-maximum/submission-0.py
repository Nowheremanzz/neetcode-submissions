class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maximum = []
        res = []
        l = 0
        for r in range(len(nums)):
            if maximum:
                while maximum[-1][1] < nums[r]:
                    maximum.pop()
                    if not maximum:
                        break
            maximum.append([r, nums[r]])
            if r - l + 1 == k:
                res.append(maximum[0][1])
                l += 1
            if maximum[0][0] < l:
                maximum.pop(0)
        return res