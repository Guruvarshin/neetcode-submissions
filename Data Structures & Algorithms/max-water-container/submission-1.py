class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        n=len(heights)
        r=n-1
        tot=0
        while l<=r:
            s=min(heights[l],heights[r])
            p=r-l
            if tot<s*p:
                tot=s*p
            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1
        return tot