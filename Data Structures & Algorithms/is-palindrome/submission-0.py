class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        for i in s:
            if not i.isalnum():
                s=s.replace(i,"",1)
        print(s)
        return s==s[::-1]
