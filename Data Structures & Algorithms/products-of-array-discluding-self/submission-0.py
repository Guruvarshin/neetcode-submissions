class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p=nums[0]
        n=len(nums)
        l=[1]*n
        for i in range(1,n):
            l[i]=p
            p*=nums[i]
        p=nums[n-1]
        for i in range(n-2,-1,-1):
            l[i]*=p
            p*=nums[i]
        return l
