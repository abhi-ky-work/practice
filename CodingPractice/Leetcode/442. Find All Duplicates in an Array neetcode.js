
/**
 * 442. Find All Duplicates in an Array neetcode
 * https://leetcode.com/problems/find-all-duplicates-in-an-array/
 * @param {number[]} nums
 * @return {number[]}
 */
 var findDuplicates = function(nums) {
    res = []
    for(let i = 0 ; i< nums.length ; i++){
        let ind = Math.abs(nums[i])-1
        if( nums[ind] < 0){
            res.push(Math.abs(nums[i]))
        }else{
            nums[ind] = -nums[ind]
        }
    }
    return res
};