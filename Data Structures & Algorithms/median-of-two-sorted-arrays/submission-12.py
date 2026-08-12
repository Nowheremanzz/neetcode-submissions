class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if (len(nums1) + len(nums2)) % 2 == 0:
            even = True
        else:
            even = False
        left_num = (len(nums1) + len(nums2)) // 2
        l, r = 0, len(nums1) - 1
        nums1.append(float("inf"))
        nums2.append(float("inf"))
        while l <= r:
            m = l + (r - l) // 2
            m_2 = left_num - m - 2
            if m + 1 > left_num:
                m -= 1 
            l1 = -float("inf") if m < 0 else nums1[m]
            l2 = -float("inf") if m_2 < 0 else nums2[m_2]
            r1 = nums1[m + 1]
            r2 = nums2[m_2 + 1]
            if r2 < l1:
                r = m - 1
            elif r1 < l2:
                l = m + 1
            elif r2 >= l1 and r1 >= l2:
                break
        m = l + (r - l) // 2
        m_2 = left_num - m - 2
        if m + 1 > left_num:
                m -= 1 
        l1 = -float("inf") if m < 0 else nums1[m]
        l2 = -float("inf") if m_2 < 0 else nums2[m_2]
        r1 = nums1[m + 1]
        r2 = nums2[m_2 + 1]
        if even:
            return (max(l1, l2) + min(r1, r2)) / 2
        else:
            return float(min(r1, r2))