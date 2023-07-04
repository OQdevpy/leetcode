url = "https://leetcode.com/problems/excel-sheet-column-number/"
columnTitle = input("Enter column title: ")
characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
sum = 0
for i in range(len(columnTitle)):
    sum += (26**i)*(characters.index(columnTitle[-1-i])+1)
print(sum)