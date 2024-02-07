class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        l1 = {}
        for i in arr:
            if i in l1:
                l1[i] += 1
            else:
                l1[i] = 1

        
        sorted_freq = sorted(l1.items(), key=lambda x: x[1])

        # Remove k elements starting from the least frequent
        for key, value in sorted_freq:
            if k >= value:
                k -= value
                del l1[key]
            else:
                break           
        return len(l1)
        