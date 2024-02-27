class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left=0
        right=0
        l1=[]
        for i in range(len(nums)):
            left=sum(nums[:i])
            right=sum(nums[i+1:])
            l1.append(abs(left-right))
        return l1