'''Given a set of positive numbers, find if we can partition it into two subsets such that the sum of elements in both the subsets is equal.

Example 1: #
Input: {1, 2, 3, 4}
Output: True
Explanation: The given set can be partitioned into two subsets with equal sum: {1, 4} & {2, 3}'''


def subset_partition(nums):
  S = sum(nums)
  if S%2 == 1:
    return False
 n = len(nums)   
 s = int(S/2)
 dp = [[False for _ in range(s+1)] for _ in range(n)]
 
 for i in range(0,n):
  dp[i][0] = True
  
 for j in range(1,s+1):
  if nums[0] == j:
    dp[0][j] = True
 
 for i in range(1,n):
  for j in range(1,s+1):
    if dp[i-1][s] == True:
      dp[i][s] = True
    elif s>num[i]:
      dp[i][s] = dp[i-1][s-num[i]]
 return dp[n-1][s]
  
