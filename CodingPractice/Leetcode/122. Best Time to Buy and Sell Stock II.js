/**
 * 122. Best Time to Buy and Sell Stock II
 * https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

 * @param {number[]} prices
 * @return {number}
 */
 var maxProfit = function(prices) {
    profits = 0
    for( r = 0 ; r < prices.length-1 ; r++){
        if( prices[r+1] > prices[r] ){
            profits += prices[r+1] - prices[r]
        }
    }
    return profits
};