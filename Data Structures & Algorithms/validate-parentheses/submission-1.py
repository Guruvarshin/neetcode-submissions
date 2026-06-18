class Solution:
    def isValid(self, s: str) -> bool:
        li=[]
        for i in s:
            if i=='(' or i=='[' or i=='{':
                li.append(i)
            elif i==')':
                if li and li[-1]=='(':
                    li.pop()
                else:
                    return False
            elif i==']':
                if li and li[-1]=='[':
                    li.pop()
                else:
                    return False
            elif i=='}':
                if li and li[-1]=='{':
                    li.pop()
                else:
                    return False
        return len(li)==0