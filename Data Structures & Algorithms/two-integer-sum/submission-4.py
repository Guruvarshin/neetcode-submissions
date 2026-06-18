class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        li=[]
        for j,i in enumerate(nums):
            if target-i in nums[j+1:]:
                n=j+1+nums[j+1:].index(target-i)
                return [j,n]
        return li