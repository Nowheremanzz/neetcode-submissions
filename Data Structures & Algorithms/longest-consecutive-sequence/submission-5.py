class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest_len = 0
        for num in s:
            length = 0
            if num - 1 in s:
                continue
            else:
                curr = num
                while curr in s:
                    curr += 1
                    length += 1
            longest_len = max(longest_len, length)
        return longest_len
