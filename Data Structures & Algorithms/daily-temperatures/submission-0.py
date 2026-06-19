class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        li=[]
        res=[0]*len(temp)
        for i,n in enumerate(temp):
            while li and temp[li[-1]]<n:
                p=li.pop()
                res[p]=i-p
            li.append(i)
        return res