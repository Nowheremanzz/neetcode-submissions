class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        s_copy = set(nums)
        longest_length = 0
        for num in s:
            length = 1
            if num in s_copy:
                s_copy.discard(num)
                increase = num + 1
                decrease = num - 1
                while 1:
                    if increase in s_copy:
                        s_copy.discard(increase)
                        length += 1
                        increase += 1
                    else:
                        break
                while 1:
                    if decrease in s_copy:
                        s_copy.discard(decrease)
                        length += 1
                        decrease -= 1
                    else:
                        break
                longest_length = max(length, longest_length)
        return longest_length
