url = "https://leetcode.com/problems/power-of-two/"
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n and not (n & n - 1)
    
    # or 
    # faster
    # if n == 0: return False
    #     return n == 1 or (n % 2 == 0 and self.isPowerOfTwo(n // 2))


a = Solution()
print(a.isPowerOfTwo(16))
