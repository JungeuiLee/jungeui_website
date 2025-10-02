class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        return profit

test = Solution()
print(test.maxProfit(prices = [7,1,5,3,6,4]))
print(test.maxProfit(prices = [7,6,4,3,1]))
print(test.maxProfit(prices = [1,2,3,4,5]))

#[7, [1,5], [3,6], 4]