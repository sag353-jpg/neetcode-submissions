class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ax = {
            0 : prices[0],
            len(prices) - 1 : prices[len(prices) - 1] 
        }
        mins = {
            0 : prices[0],
            len(prices) - 1 : prices[len(prices) - 1]
        }
        if len(prices) == 1:
            return 0
        for i in range(1, len(prices) - 1):
                if prices[i] >= prices[i-1] and prices[i] >= prices[i+1]:
                    ax[i] = prices[i]
                if prices[i] <= prices[i-1] and prices[i] <= prices[i+1]:
                    mins[i] = prices[i]
        target = []
        for keymax in ax:
            for keymin in mins:
                if keymin < keymax:
                    target.append(ax[keymax] - mins[keymin])
        value = max(target)
        if value <= 0:
            return 0
        return value
    

