class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
    
        for customer in accounts:
            wealth = sum(customer)  # Calculate the wealth for the current customer
            max_wealth = max(max_wealth, wealth)  # Update max_wealth if necessary
    
        return max_wealth
    
        