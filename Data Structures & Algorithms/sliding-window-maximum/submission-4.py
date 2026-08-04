class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maximum = deque()
        res = []
        l = 0
        for r in range(len(nums)):
            while maximum and nums[maximum[-1]] <= nums[r]:
                maximum.pop()
            maximum.append(r)
            if r - l + 1 == k:
                res.append(nums[maximum[0]])
                l += 1
            if maximum[0] < l:
                maximum.popleft()
        return res