class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        l1 = []
        for i in range(len(nums)):
            cnt = 0
            for j in range(len(nums)):
                if i != j and nums[j] < nums[i]:
                    cnt += 1
            l1.append(cnt)
        return l1

        