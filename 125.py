url = "https://leetcode.com/problems/valid-palindrome/"
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = ''.join(e for e in s if e.isalnum())
        return s == s[::-1]

if __name__ == "__main__":
    a= Solution()
    print(a.isPalindrome("race a car"))