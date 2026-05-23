class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lo=0
        n=set(nums)
        for i in n:
            if i-1 not in n:
                l=1
                while i+l in nums:
                    l+=1
                lo=max(l,lo)
        return lo
            