class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pr=0
        buy=float('inf')
        for i in prices:
            if buy>i:
                buy=i
            if pr<(i-buy):
                pr=i-buy
        return pr