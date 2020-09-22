"""
Say you have an array for which the ith element is the price of a given stock on day i.
If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.
Input: [7,1,5,3,6,4]
Output: 5
"""
def maxProfit(prices):
    profit = 0
    min = 9999999
    for i in range(0,len(prices)):
        if prices[i]<min:
            min = prices[i]
        if prices[i]-min > profit:
            profit = prices[i] - min
    print("mim=",min)
    return profit

prices = [7,1,5,3,6,4]
print("output:",maxProfit(prices))
