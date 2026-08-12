class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1
        n1, n2 = len(nums1), len(nums2)
        left_num = (n1 + n2) // 2
        l, r = 0, n1
        while l <= r:
            i = l + (r - l) // 2
            j = left_num - i
            l1 = -float("inf") if i == 0 else nums1[i - 1]
            l2 = -float("inf") if j == 0 else nums2[j - 1]
            r1 = float("inf") if i == n1 else nums1[i]
            r2 = float("inf") if j == n2 else nums2[j]
            if r2 >= l1 and r1 >= l2:
                if (n1 + n2) % 2 == 1:
                    return min(r1, r2)
                else:
                    return (max(l1, l2) + min(r1, r2)) / 2
            elif r2 < l1:
                r = i - 1
            elif r1 < l2:
                l = i + 1