class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)  # Find the maximum number of candies among all kids
        result = []  # Create an empty list to store the results
        
        for i in candies:
            if i + extraCandies >= max_candies:
                result.append(True)
            else:
                result.append(False)
        return result
            
        