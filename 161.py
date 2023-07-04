url = "https://leetcode.com/problems/excel-sheet-column-title/description/"
columnNumber = int(input("Enter column number: "))

characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
result = characters[columnNumber%26-1] if columnNumber<26 else characters[columnNumber//26-1]+characters[columnNumber%26-1]
print(result)
