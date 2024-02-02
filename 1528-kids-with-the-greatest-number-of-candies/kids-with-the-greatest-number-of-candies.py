class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        greatest = max(candies)  
        k = [] 
        
        for i in candies:
            if i + extraCandies >= greatest:
                k.append(True)
            else:
                k.append(False)
        return k
            
        