class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        cnt=0
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[i]==nums[j]:
                    cnt+=1
        return cnt            

        