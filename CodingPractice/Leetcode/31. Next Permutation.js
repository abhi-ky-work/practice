/**
 * 31. Next Permutation
 * https://leetcode.com/problems/next-permutation/
 * @param {number[][]} matrix
 * @return {number[]}
 */
 
 // [1,2,6,5,4]
var nextPermutation = function(nums) {

    let i = nums.length -2
    while(i >= 0 && nums[i+1] <= nums[i]){
        i--
    }
    if( i >= 0){
        let j = nums.length - 1
        while( nums[j] <= nums[i]){
            j--
        }
        swap(nums,i, j)

    }
    reverse(nums, i+1, nums.length -1)
};
function swap(nums, i , j){
    [nums[i],nums[j]] = [nums[j], nums[i]]
}
function reverse(nums, l , r){
    while( l < r){
        [nums[l], nums[r]]=[nums[r], nums[l]]
        l++
        r--
    }
}