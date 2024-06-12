class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts={}
        l1=[[] for i in range(0,len(nums)+1)]
        for num in nums:
            counts[num]=1+counts.get(num,0)
        res=[]
        for num,count in counts.items():
            l1[count].append(num)
        
        for i in range(len(l1)-1,0,-1):
            for j in l1[i]:
                res.append(j)
                if len(res)==k:
                    return res

        