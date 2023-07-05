url = "https://leetcode.com/problems/shortest-palindrome/"
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return s
        for i in range(len(s), 0, -1):
            if s[:i] == s[:i][::-1]:
                return s[i:][::-1] + s
        return s[1:][::-1] + s
    