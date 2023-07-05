class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if haystack==needle:
            return 0
        if needle in haystack:
            return haystack.index(needle)
        for i in range(len(haystack)-len(needle)):
            if needle==haystack[i:i+len(needle)]:
                return i
        return -1