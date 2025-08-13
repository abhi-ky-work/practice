
/**
190. Reverse Bits
https://leetcode.com/problems/reverse-bits
 * @param {number} n - a positive integer
 * @return {number} - a positive integer
 */
var reverseBits = function(n) {
    res = 0
    re = ""
    console.log(n.toString(2))
    for( i = 0 ; i < 32 ; i++){
        bit = (n >> i) & 1
        res = res | (bit << (31 - i))
    }
    return res >>> 0
};


/**
 * @param {number} n - a positive integer
 * @return {number} - a positive integer
 */
// var reverseBits = function(n) {
//     return parseInt(n.toString(2).split('').reverse().join('').padEnd(32, '0'), 2)
// };

// var reverseBits = function(n) {
//     let rev = 0;
//     for (let i = 31; i>=0; i--) {
//         rev += (n&1)<<i
//         n >>=1
//     }
//     return rev>>>0
// };

