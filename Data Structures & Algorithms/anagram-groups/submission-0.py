class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm={}
        for i in strs:
            s="".join(sorted(i))
            if s not in hm:
                hm[s]=[]
            hm[s].append(i)
        li=[]
        for i in hm:
            li.append(hm[i])
        return li