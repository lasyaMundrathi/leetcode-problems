class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)
        for str_ in strs:
            count=[0]*26
            for char in str_:
                count[ord(char)-ord('a')]+=1
            res[tuple(count)].append(str_)
        return res.values()

