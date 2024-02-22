class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0  # Initialize the first pointer for the position of the last unique element
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1  # Move the unique element's index forward
                nums[i] = nums[j]  # Place the new unique element at the next position
    
        return i + 1  # Return the number of unique elements, which is the index + 1
                
     