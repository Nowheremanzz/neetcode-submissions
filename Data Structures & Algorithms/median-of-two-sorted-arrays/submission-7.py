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
            if m_2 == -1:
                if nums1[m] <= nums2[0]:
                    break
                else:
                    r = m - 1
            if m_2 == -2:
                return float(nums1[m])
            if nums2[m_2 + 1] < nums1[m]:
                r = m - 1
            elif nums1[m + 1] < nums2[m_2]:
                l = m + 1
            elif nums2[m_2 + 1] >= nums1[m] and nums1[m + 1] >= nums2[m_2]:
                break
        m = l + (r - l) // 2
        m_2 = left_num - m - 2
        if even:
            return (max(-float("inf") if m < 0 else nums1[m], -float("inf") if m_2 < 0 else nums2[m_2]) + min(nums1[m + 1], nums2[m_2 + 1])) / 2
        else:
            return float(min(nums1[m + 1], nums2[m_2 + 1]))

        

            