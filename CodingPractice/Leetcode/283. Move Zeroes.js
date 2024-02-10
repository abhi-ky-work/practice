/**
 * 283. Move Zeroes
 * https://leetcode.com/problems/move-zeroes/
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var moveZeroes = function(nums) {
    let l = 0
    while(l < nums.length && nums[l] != 0){
        l++
    }
    let r = l
    for(r = l+1 ; r < nums.length ; r++){
        if( nums[r] ){
            [nums[l], nums[r]] = [nums[r], nums[l]]
            l ++
        }
    }
};