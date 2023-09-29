'''
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock 
at any time. However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.
Example 2:

Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Total profit is 4.
Example 3:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.
'''

'''
solution
1.initially we declare profit variable to 0
2.then we declare min_value to prices[0]
3.we will run the loop from index 1 till its length
4.if the current value is less than min value
5.then we assign that value to min value
6.otherwise add the value after subtracting the current value to the min value to the profit
7.assign the current value to the min value
8. finally return the profit
'''

#solution
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        if len(prices)==0:
            return 0
        elif len(prices)==1:
            return 0
        else:
            min_value=prices[0]
            for i in range(1,len(prices)):
                if prices[i]<min_value:
                    min_value=prices[i]
                else:
                    profit=profit+prices[i]-min_value
                    min_value=prices[i]
            return profit
        
