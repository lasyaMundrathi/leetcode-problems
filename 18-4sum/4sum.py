from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        result = []

        for a in range(n - 3):
            # Skip duplicates
            if a > 0 and nums[a] == nums[a - 1]:
                continue

            for b in range(a + 1, n - 2):
                # Skip duplicates
                if b > a + 1 and nums[b] == nums[b - 1]:
                    continue

                left = b + 1
                right = n - 1

                while left < right:
                    total = nums[a] + nums[b] + nums[left] + nums[right]

                    if total == target:
                        result.append([nums[a], nums[b], nums[left], nums[right]])
                        # Skip duplicates
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif total < target:
                        left += 1
                    else:
                        right -= 1

        return result
