'''
fraction of item is not allowed
given N items weight and profit 
we can keep these item in knapsack with capacity c

find the maximum profit can be made with keeping things in kapsack


approach:
it is a straight permutation question

at every step you will either take it or leave it, keeping the capacity in mind
and after trying all the combination you will get the one with max profit under the weight criteria
'''

items = [[31, 3], [26, 1], [72,5], [17,7]] # [[profit , weight]]

profits = [31, 26, 72, 17]
weights = [ 3,  1,  5,  7]   # wight 5 , 1 ( 72 + 26)
capacity = 7


def max_profit(i, profits, weights, capacity):
    if i >= len(profits) or capacity <= 0 :
        return 0
    profit1 = 0
    if weights[i] <= capacity:
        profit1 = profits[i] + max_profit(i + 1, profits, weights, capacity - weights[i])

    profit2 = max_profit(i+1, profits, weights, capacity)

    return max(profit1, profit2)


print("Max profit from knapsack is : ", max_profit(0, profits, weights, 7))