/**
 * 121. Best Time to Buy and Sell Stock
 * https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

 * @param {number[]} prices
 * @return {number}
 */
 var maxProfit = function(prices) {
    let max = 0
    let l = 0
    for(let r = 1; r < prices.length ; r++){
        let diff = prices[r] - prices[l]
        max = Math.max(max,diff)
        if( diff < 0){
            l = r
        }
        
    }
    return max 
};