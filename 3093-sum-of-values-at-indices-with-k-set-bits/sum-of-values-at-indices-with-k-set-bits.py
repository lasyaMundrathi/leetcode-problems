class Solution:
    def count_set_bits(self, n):
        count = 0
        while n:
            count += n & 1
            n >>= 1
        return count

    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        total_sum = 0
        for i, num in enumerate(nums):
            if self.count_set_bits(i) == k:
                total_sum += num
        return total_sum      