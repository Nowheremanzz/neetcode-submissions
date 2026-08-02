class Solution:
    def trap(self, height: List[int]) -> int:
        volume = 0
        l, r = 0, len(height)-1
        l_max, r_max = height[l], height[r]
        while l < r:
            if l_max <= r_max:
                volume += l_max - height[l]
                l += 1
                l_max = max(l_max, height[l])
            elif r_max < l_max:
                volume += r_max - height[r]
                r -= 1
                r_max = max(r_max, height[r])
        return volume
