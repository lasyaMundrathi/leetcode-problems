class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged_array=nums1+nums2
        merged_array.sort()
        total=len(merged_array)
        if total%2 ==1:
            return float(merged_array[total//2])
        else:
            return ( float(merged_array[total//2 -1]) + float(merged_array[total//2]) ) / 2.0
