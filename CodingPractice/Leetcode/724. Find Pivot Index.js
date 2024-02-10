/** 
 * 724. Find Pivot Index
 * https://leetcode.com/problems/find-pivot-index/
 * @param {number[]} nums
 * @return {number}
 */


 var pivotIndex = function(nums) {
    let len = nums.length 
    let revsum = nums[len - 1]
    let sum = nums[0]
    let revarr = Array(len).fill(0)
    revarr[len-1] = revsum
    let arr = [sum]
    for( let i = 1 ; i < len ; i++){
        arr.push(sum += nums[i])
        revarr[len - i - 1] = (revsum += nums[len - i - 1])
    }
    for(let i = 0 ; i < len ; i ++){
        if( arr[i] == revarr[i]){
            return i
        }
    }
    return -1
};



/** 724. Find Pivot Index

 * @param {number[]} nums
 * @return {number}
 */
 var pivotIndex = function(nums) {
    let tsum = nums.reduce( (res ,item)=> res + item , 0 )
    let sum = 0
    for( let i = 0 ; i < nums.length ; i++){
        tsum -= nums[i]
        if( tsum == sum) return i;
        sum += nums[i]
    }
    return -1
};
