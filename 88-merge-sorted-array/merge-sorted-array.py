class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        x=0
        for i in range(n):
            nums1[m+i]=nums2[x]
            x+=1
        return nums1.sort()

        