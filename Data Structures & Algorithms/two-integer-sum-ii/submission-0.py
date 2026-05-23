class Solution:
    def twoSum(self, num: List[int], target: int) -> List[int]:
        l=[]
        for i,n in enumerate(num):
            j=target-n
            if j in num[:i]:
                l.append(num.index(j)+1)
                l.append(i+1)
                return l
        return l