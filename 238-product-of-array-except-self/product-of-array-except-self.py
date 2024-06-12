class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre_fix,post_fix=1,1
        res=[1]*len(nums)
        for i in range(len(nums)):
            res[i]*=pre_fix
            pre_fix*=nums[i]

        for i in range(len(nums)-1,-1,-1):
            res[i]*=post_fix
            post_fix*=nums[i]
        return res


        