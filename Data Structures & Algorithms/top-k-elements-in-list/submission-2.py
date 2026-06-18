class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm={}
        for i in nums:
            if i not in hm:
                hm[i]=0
            hm[i]+=1
        st=[k for k,v in sorted(hm.items(), key=lambda i:i[1])]
        return st[-k:]