/**
 * 532. K-diff Pairs in an Array.js
 * https://leetcode.com/problems/k-diff-pairs-in-an-array/
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
 var findPairs = function(nums, k) {
    let map = { }
    for(let i = 0 ; i < nums.length ; i ++){
        let num = nums[i]
        if( map[num]){
            map[num] += 1
        }else{
            map[num] = 1
        }
    }
    let keys = Object.keys(map)
    let count = 0
    for(let j = 0 ; j < keys.length ; j++){
        let key = keys[j]
        if( map[parseInt(key) +k]){
            if( k === 0 ){
                if( map[key] > 1 ){
                count++
                }
            }else{
                count++
            }
        }
    }
    return count
};