url = "https://leetcode.com/problems/best-time-to-buy-and-sell-stock/"
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = float('inf')
        maxProfit = 0
        for i in prices:
            if i < minPrice:
                minPrice = i
            elif i - minPrice > maxProfit:
                maxProfit = i - minPrice
        return maxProfit
    
if __name__ == "__main__":
        
        a = Solution()
        prices = [7,6,4,3,1]
        print(a.maxProfit(prices))