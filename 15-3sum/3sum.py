class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        l1 = []
        n = len(nums)
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # Skip duplicates for the first element of the triplet

            left, right = i + 1, n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < 0:
                    left += 1  # Need a larger number
                elif total > 0:
                    right -= 1  # Need a smaller number
                else:
                    # Found a triplet
                    l1.append([nums[i], nums[left], nums[right]])
                    
                    # Skip duplicates for the second and third elements of the triplet
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

        return l1
