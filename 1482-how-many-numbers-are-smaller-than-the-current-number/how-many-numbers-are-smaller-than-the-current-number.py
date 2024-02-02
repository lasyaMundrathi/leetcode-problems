class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        i=0
        l1=[]
        while i <len(nums):
            cnt=0
            j=0
            while j<len(nums):
                if (j!=i) and nums[j]<nums[i]:
                    cnt+=1
                j+=1    
            l1.append(cnt)
            i+=1
        return l1

        