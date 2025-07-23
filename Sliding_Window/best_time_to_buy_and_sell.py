'''
Problem: Best Time to Buy and Sell Stock
-------

You are given an integer array `prices` where `prices[i]` is the price of NeetCoin on
the `ith` day.

You may choose a single day to buy one NeetCoin and choose a different day in the
future to sell it.

Return the maximum profit you can achieve. You may choose to not make any transactions,
in which case the profit would be `0`.

-------
URL: https://neetcode.io/problems/buy-and-sell-crypto?list=neetcode150
'''

def maxProfit(prices: list[int]) -> int:
    # We want to track the total possible profit we could make at each step. 
    # We take a minimum for the price and calculate the possible profit at each step.

    profit = 0
    curr_price = prices[0]
    for price in prices:
        curr_price = min(curr_price, price)
        profit = max(profit, price - curr_price)
    return profit
    
    
    
def test1(prices: list[int] = [10,1,5,6,7,1]):
    sol = 6
    print('Test 1: PASSED' if maxProfit(prices) == sol else 'Test 1: FAILED')
    
def test2(prices: list[int] = [10,8,7,5,2]):
    sol = 0
    print('Test 2: PASSED' if maxProfit(prices) == sol else 'Test 2: FAILED')
    
test1()
test2()