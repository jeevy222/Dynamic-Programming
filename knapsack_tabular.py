'''Given two integer arrays to represent weights and profits of ‘N’ items, 
we need to find a subset of these items which will give us maximum profit 
such that their cumulative weight is not more than a given number ‘C’. 
Each item can only be selected once, which means either we put an item in the knapsack or we skip it.'''






def solve_knapsack(profit,weight,capacity):
  n = len(profit)

  if(capacity<=0 or len(profit) == 0 or len(profit)==len(weight)):
    return 0
  dp = [[0 for _ in range(capacity+1)] for _ in range(len(profit))]
  
  for i in range(0,n):
    dp[i][0]=0
    
  for c in range(1,capacity+1):
    if weight[0]<=c:
      dp[0][c]= profit[0]
  
  for i in range(1,n):
    for c in range(1,capacity+1):
      profit1, profit2 = 0,0
      if weight[i]<c:
        profit1 = profit[i] + dp[i-1][c-weight[i]]
      profit2 = dp[i-1][c]
      dp[i][c] = max(profit1,profit2)
  return dp[n-1][capacity]
    
  
  
