# 11 may 2026
# median od two sorted array
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        lst = []
        i,j = 0,0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                lst.append(nums1[i])
                i += 1
            else:
                lst.append(nums2[j])
                j += 1 
        while i < len(nums1):
            lst.append(nums1[i])
            i += 1    
        while j < len(nums2):
            lst.append(nums2[j])
            j += 1 

        if len(lst)%2 != 0:
            return lst[len(lst)//2]
        else:
            # 0 1 2 3 4 5
            idx = len(lst)//2
            return (lst[idx] + lst[idx-1]) / 2.0