class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm={}
        for i in strs:
            y="".join(sorted(i))
            if y not in hm:
                hm[y]=[]
            hm[y].append(i)
        li=[]
        li.extend(hm.values())
        return li