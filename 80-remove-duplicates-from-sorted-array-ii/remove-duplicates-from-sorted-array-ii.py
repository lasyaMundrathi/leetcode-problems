class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for i in nums:
            while nums.count(i)>2:
                nums.remove(i)






        #   def removeDuplicates(self, nums: List[int]) -> int:
        # i = 0  # Initialize the first pointer for the position of the last unique element
        # while i < len(nums)-1:
        #     if nums[i] == nums[i + 1]:
        #         nums.pop(i)
        #     else:
        #         i += 1
        # return len(nums)