'''Given an infinite supply of ‘n’ coin denominations and a total money amount, 
we are asked to find the minimum number of coins needed to make up that amount.

Example 1:

Denominations: {1,2,3}
Total amount: 5
Output: 2
Explanation: We need minimum of two coins {2,3} to make a total of '5'
Example 2:

Denominations: {1,2,3}
Total amount: 11
Output: 4
Explanation: We need minimum four coins {2,3,3,3} to make a total of '11'. '''

import math
def coin_change(denominations,total):
  n = len(denominations)
  
  dp = [[math.inf for _ in range(total+1)] for _ in range(n)]
  
  for i in range(n):
    dp[i][] == 0
  
  for i in range(n):
    for amount in range(total+1):
      dp[i][amount] = dp[i-1][amount]
      if denominations[i] < amount and if dp[i][amount - denominations[i]] != math.inf:
        dp[i][amount] = min(dp[i-1][amount], dp[i][amount - denominations[i]] +1)
  return dp[n-1][total] if dp[n-1][total] != math.inf else -1
        
