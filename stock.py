class Solution(object):
    def maxProfit(self,prices):
        min_price,max_profit=1000000,0
        for price in prices:
            min_price=min(min_price,price)
            max_profit=max(max_profit,price-min_price)
        return max_profit

#a=Solution()
#print a.maxProfit([1, 2, 3, 0, 2])

class Solution2(object):
    def maxProfit(self,prices):
        res=0
        for i in range(1,len(prices)):
            if prices[i]>prices[i-1]:
                res+=prices[i]-prices[i-1]
        return res
        
#a=Solution2()
#print a.maxProfit([1, 2, 3, 0, 2])

class Solution3(object):
    def maxProfit(self,prices):
        min_price=100000
        max_profit=0
        max_profits=[]
        for price in prices:
            min_price=min(min_price,price)
            max_profit=max(max_profit,price-min_price)
            max_profits.append(max_profit)
        
        max_price_after=-1
        max_profit_after=0
        res=0
        for i in range(len(prices)-1,-1,-1):
            max_price_after=max(max_price_after,prices[i])
            max_profit_after=max(max_profit_after,max_price_after-prices[i])
            res=max(res,max_profits[i]+max_profit_after)
        return res
            
#a=Solution3()
#print a.maxProfit([1, 2, 3, 0, 2])

class Solution32(object):
    def maxProfit(self,prices):
        if not prices: return 0
        hold=[0]*len(prices)
        sold=[0]*len(prices)
        hold[0]=-prices[0]
        sold[0]=0
        for i in range(1,len(prices)):
            hold[i] = max(hold[i-1], sold[i-2]-prices[i] if i>1 else -prices[i])
            sold[i] = max(sold[i-1], hold[i-1]+prices[i])
        return sold[-1]
        
a=Solution32()
print a.maxProfit([1, 2, 3, 0, 2])

class Solution4(object):
    def maxProfit(self,k,prices):
        if k*2>=len(prices):
            profit=0
            for i in range(1,len(prices)):
                profit+=max(0,prices[i]-prices[i-1])
            return profit
        else:
            dp=[0]+[None]*(k*2)
            for i in range(len(prices)):
                for j in range(1,min(i,2*k)+1): # regard time i as the jth transaction
                    dp[j]=max(dp[j],dp[j-1]+prices[i]*[1,-1][j%2])
            return max(dp)