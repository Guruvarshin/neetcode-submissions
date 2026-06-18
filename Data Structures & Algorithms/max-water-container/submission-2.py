class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        n = len(heights)
        r=n-1
        mi=0
        while l<=r:
            le=min(heights[l],heights[r])
            bre=r-l
            mi=max(mi,le*bre)
            if heights[l]<heights[r]:
                l=l+1
            else:
                r=r-1
        return mi