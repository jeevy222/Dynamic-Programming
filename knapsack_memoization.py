'''Given two integer arrays to represent weights and profits of ‘N’ items, 
we need to find a subset of these items which will give us maximum profit 
such that their cumulative weight is not more than a given number ‘C’. 
Each item can only be selected once, which means either we put an item in the knapsack or we skip it.'''






def solve_knapsack(profit,weight,capacity):
  dp = [[-1 for _ in range(capacity+1)] for _ in range(len(profit))]
  return knapsack_memoization(dp,profit,weight,capacity,0)
  
def knapsack_memoization(dp,profit,weight,capacity,currentindex):
  
  if capacity<=0 or currentindex>=len(profit):
    return 0
  
  if dp[currentindex][capacity]==-1:
    profit1 = 0
    if weight[currentindex] <= capacity:
      profit1 = profit[currentindex] +  knapsack_memoization(dp,profit,weight,capacity-profit[currentindex],currentindex+1)
    profit2 = knapsack_memoization(dp,profit,weight,capacity,currentindex+1)
    dp[currentindex][capacity = max(profit1,profit2)
  return dp[currentindex][capacity]
   
