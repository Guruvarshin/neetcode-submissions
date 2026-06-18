class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hm={}
        l=0
        r=0
        n=len(s)
        maxi=0
        while r<n:
            print(hm)
            if s[r] in hm:
                z=hm[s[r]]
                while l<=z:
                    del hm[s[l]]
                    l+=1
            hm[s[r]]=r
            if r-l+1>maxi:
                maxi=r-l+1
            r+=1
        return maxi
