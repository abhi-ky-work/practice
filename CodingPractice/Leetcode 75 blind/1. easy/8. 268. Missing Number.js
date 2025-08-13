/**
268. Missing Number
https://leetcode.com/problems/missing-number/?envType=problem-list-v2&envId=psz78mq6&favoriteSlug=&difficulty=EASY
 * @param {number[]} nums
 * @return {number}
 */
var missingNumber = function(nums) {
    let arr = Array(nums.length + 1).fill(null)
    for(let i = 0 ; i < nums.length ; i++){
        arr[nums[i]] = nums[i]
    }
    let result = -1
    for(let i = 0 ; i < arr.length ; i++){
        if(arr[i] == null){
            result = i 
            // console.log("Result is " , i)
            return i
        }
    }
    
};