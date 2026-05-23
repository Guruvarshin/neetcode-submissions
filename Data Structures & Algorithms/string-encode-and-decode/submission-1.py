class Solution:

    def encode(self, strs: List[str]) -> str:
        s=""
        for i in strs:
            s+=i
            s+='~'
        return s
    def decode(self, s: str) -> List[str]:
        return s.split("~")[:-1]