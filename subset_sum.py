'''Given a set of positive numbers, determine if there exists a subset whose sum is equal to a given number ‘S’.

Example 1: #
Input: {1, 2, 3, 7}, S=6
Output: True
The given set has a subset whose sum is '6': {1, 2, 3}'''

def subset_sum(nums,SUM):
  n = len(nums)
  dp = [[False for _ in range(SUM+1)] for _ in range(n)]
  
  for i in range(0,n):
    dp[i][0] = True
  
  for s in range(1,SUM+1):
    if s==nums[0]:
      dp[0][s]=True
  
  for i in range(1,n):
    for s in range(1,SUM+1):
      if dp[i-1][s] is True:
        dp[i][s] = True
      elif s>nums[i]:
        dp[i][s] = dp[i-1][s-nums[i]]
  return dp[n-1][SUM]
    
    
