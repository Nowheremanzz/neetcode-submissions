class Solution:
    def trap(self, height: List[int]) -> int:
        l_max = [0] * len(height)
        r_max = [0] * len(height)
        maximum = 0
        for i in range(len(height)):
            l_max[i] = maximum
            maximum = max(maximum, height[i])
        maximum = 0
        for i in range(len(height)-1, -1, -1):
            r_max[i] = maximum
            maximum = max(maximum, height[i])
        volume = 0
        for i in range(len(height)):
            water = min(l_max[i], r_max[i]) - height[i]
            if water < 0:
                water = 0
            volume += water
        return volume
