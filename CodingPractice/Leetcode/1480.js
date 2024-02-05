/** 1480. Running Sum of 1d Array
 * @param {number[]} nums
 * @return {number[]}
 */
 var runningSum = function(nums) {
    "use strict"
    for(let i = 1; i < nums.length ; i++){
        nums[i] = nums[i] + nums[i-1]
    }
    return nums
};