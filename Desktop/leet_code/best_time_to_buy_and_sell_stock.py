class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max = 0
        # for i in range(len((prices))):
        #     for j in range(i + 1, len(prices)):
        #         if (prices[j] - prices[i]) > max:
        #             max = prices[j] - prices[i]
        # return max
        i = 0
        min = prices[0]
        while i < len(prices):
            if prices[i] < min:
                min = prices[i]
            profit = prices[i] - min

            if profit > max:
                max = profit
            
            i += 1
        return max

test = Solution()
print(test.maxProfit(prices = [7,1,5,3,6,4]))
print(test.maxProfit(prices = [1,2,3,4,5]))
print(test.maxProfit(prices = [7,6,4,3,1]))