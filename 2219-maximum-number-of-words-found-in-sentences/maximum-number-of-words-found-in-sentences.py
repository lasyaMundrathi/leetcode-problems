class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        l1=[]
        for i in sentences:
            l1.append(len(i.split()))
        return max(l1)

        