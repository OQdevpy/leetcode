url = "https://leetcode.com/problems/merge-sorted-array/"
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

for j in range(n):
          nums1[m+j] = nums2[j]
nums1.sort()