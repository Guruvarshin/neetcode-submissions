class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        lm=-math.inf
        tm=-math.inf

        for i in nums:
            if lm==-math.inf:
                lm=i
            else:
                lm=max(lm+i,i)
            tm=max(lm,tm)
        return tm