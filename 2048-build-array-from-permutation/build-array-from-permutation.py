class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        l1=[]
        i=0
        for i in range(len(nums)):
            j =nums[i]
            l1.append(nums[j])
        return l1       
        