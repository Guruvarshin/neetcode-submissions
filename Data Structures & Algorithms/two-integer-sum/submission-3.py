class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans=[]
        for i,n in enumerate(nums):
            t=target-n
            if t in nums[i+1:] and nums.index(t,i+1) not in ans:
                o=nums.index(t,i+1)
                ans.append(i)
                ans.append(o)
        return ans
        