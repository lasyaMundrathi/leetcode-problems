class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        # l1=[]
        # k=0
        # for i in words:
        #     if x in i:
        #         l1.append(k)
        #     k+=1   
        # return l1
        return [i for i,word in enumerate(words) if x in word ]