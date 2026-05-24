class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l=[]
        n=len(nums)
        for i in range(n-2):
            for j in range(i+1,n-1):
                s=-(nums[i]+nums[j])
                p=nums[j+1:]
                if s in p:
                    o=sorted([nums[i],nums[j],s])
                    if o not in l:
                        l.append(o)
        return l
