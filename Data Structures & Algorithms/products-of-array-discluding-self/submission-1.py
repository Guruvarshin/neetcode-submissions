class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        li=[1]
        n=len(nums)
        for i in range(1,n):
            li.append(nums[i-1]*li[i-1])
        print(li)
        mul=nums[n-1]
        for i in range(n-2,-1,-1):
            print(mul)
            li[i]*=mul
            mul*=nums[i]
        return li
            