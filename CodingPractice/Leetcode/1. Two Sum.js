/**
 * 1. Two Sum
 * https://leetcode.com/problems/two-sum/
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
 var twoSum = function(nums, target) {
    map = new Map();
    for( let i = 0 ; i < nums.length ; i++){
        if( map.has(nums[i])){
           return [i, map.get(nums[i])]
        }
        map.set(target-nums[i], i)
    }
};