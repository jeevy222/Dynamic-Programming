'''Given a rod of length ‘n’, we are asked to cut the rod and sell the pieces in a way 
that will maximize the profit. We are also given the price of every piece of length ‘i’ where ‘1 <= i <= n’.

Example:

Lengths: [1, 2, 3, 4, 5]
Prices: [2, 6, 7, 10, 13]
Rod Length: 5'''


def rod_cutting(lengths,prices,n):
  l = len(Lengths)
  if n <= 0 or len(Prices) != l or l ==0:
    return 0
    
  dp = [[0 for _ in range(n+1)] for _ in range(l)]
  
  p1 = 0
  p2 = 0
  
  for i in range(l):
    for rod in range(n+1):
      if Lengths[i] <= rod:
        p1 = Prices[i] + dp[i][rod-Lengths[i]]
      p2 = dp[i-1][rod]
      dp[i][rod] = max(p1,p2)
  return dp[l-1][n]
   
  
