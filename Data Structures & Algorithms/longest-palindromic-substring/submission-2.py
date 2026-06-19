class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)==0:
            return ""
        maxs=s[0]
        maxi=0
        for i in range(len(s)-1):
            if i==0:
                u=self.isPalin(s,i,i+1)
                p=len(u)
                if p>maxi:
                    maxi=p
                    maxs=u
            else:
                u=self.isPalin(s,i,i)
                t=self.isPalin(s,i,i+1)
                if len(u)>maxi:
                    maxs=u
                    maxi=len(u)
                if len(t)>maxi:
                    maxs=t
                    maxi=len(t)
        return maxs
    
    def isPalin(self,s,i,j):
        if s[i]!=s[j]:
            return s[i]
        while i>=0 and j<len(s) and s[i]==s[j]:
            i-=1
            j+=1
        return s[i+1:j]
        