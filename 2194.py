url = "https://leetcode.com/problems/cells-in-a-range-on-an-excel-sheet/description/"
from typing import List
class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        
        r = ord(s[0])
        r_start = int(s[1])
        c = ord(s[3])
        c_finish = int(s[4])
        ans = []
        for i in range(r,c+1):
            for k in range(r_start,c_finish+1):
                
                ans.append(chr(i)+str(k))
        return ans
        

a= Solution()
print(a.cellsInRange("A1:B2"))
