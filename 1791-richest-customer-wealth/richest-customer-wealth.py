class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        l1=[]
        for i in accounts:
            l1.append(sum(i))

        return max(l1)
    
        