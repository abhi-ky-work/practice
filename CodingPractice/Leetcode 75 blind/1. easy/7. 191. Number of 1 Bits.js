/**
191. Number of 1 Bits 
https://leetcode.com/problems/number-of-1-bits
 * @param {number} n
 * @return {number}
 */
var hammingWeight = function(n) {
    res = 0 
    while(n){
        res += n % 2
        n = n >> 1
    }
    return res
};

var hammingWeight = function(n) {
    res = 0 
    while(n){
        n = n & (n-1)
        res += 1
    }
    return res
};