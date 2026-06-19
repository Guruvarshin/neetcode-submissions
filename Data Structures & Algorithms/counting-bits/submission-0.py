class Solution:
    def countBits(self, n: int) -> List[int]:
        li=[0]*(n+1)
        for i in range(1,n+1):
            j=0
            p=i
            while p:
                if p&1:
                    j+=1
                p=p>>1
            li[i]=j
        return li