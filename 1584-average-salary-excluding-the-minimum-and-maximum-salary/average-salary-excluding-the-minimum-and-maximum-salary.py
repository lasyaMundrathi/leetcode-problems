class Solution:
    def average(self, salary: List[int]) -> float:
        salary.remove(min(salary))
        salary.remove(max(salary))
        return mean(salary)