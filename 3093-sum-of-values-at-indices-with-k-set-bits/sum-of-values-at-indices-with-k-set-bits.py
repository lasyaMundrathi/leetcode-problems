class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        total_sum = 0
        
        # Define a function to count the number of set bits in an integer
        def count_set_bits(n):
            count = 0
            while n:
                count += n & 1
                n >>= 1
            return count
        
        # Iterate through the indices of the array
        for i, num in enumerate(nums):
            # Check if the number of set bits in the index equals k
            count = 0
            idx = i
            while idx:
                count += idx & 1
                idx >>= 1
            if count == k:
                total_sum += num
        
        return total_sum
