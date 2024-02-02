class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # n=len(nums)
        # l1=[]
        # for i in range(n):
        #     l1[i]=nums[i]
        #     l1[i+n]=nums[i]
        l1=nums+nums
        return l1

        