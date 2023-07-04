url = "https://leetcode.com/problems/excel-sheet-column-title/description/"
ans = []
while(n > 0):
    n -= 1
    curr = n % 26
    n = int(n / 26)
    ans.append(chr(curr + ord('A')))

print( ''.join(ans[::-1]))
