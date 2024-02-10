/**
 * 66. Plus One
 * https://leetcode.com/problems/plus-one/

 * @param {number[]} digits
 * @return {number[]}
 */
 var plusOne = function(digits) {
    let end = digits.length - 1
    while( end > -1 && digits[end] == 9){
        digits[end] = 0
        end --
    }
    if( end == -1){
        return [1, ...digits]
    }
    digits[end] += 1
    return digits
    
};