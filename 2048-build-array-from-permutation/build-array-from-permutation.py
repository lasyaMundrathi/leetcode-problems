class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        l1=[]
        i=0
        for i in range(len(nums)):
            l1.append(nums[nums[i]])
        return l1       
        