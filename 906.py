url = "https://leetcode.com/problems/super-palindromes/"
class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        left, right = int(left), int(right)
        ans = 0
        for i in range(100000):
            s = str(i)
            t = s + s[-2::-1]
            v = int(t) ** 2
            if v > right:
                break
            if v >= left and str(v) == str(v)[::-1]:
                ans += 1
        for i in range(100000):
            s = str(i)
            t = s + s[::-1]
            v = int(t) ** 2
            if v > right:
                break
            if v >= left and str(v) == str(v)[::-1]:
                ans += 1
        return ans
    
