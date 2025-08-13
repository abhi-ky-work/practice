/**
70. Climbing Stairs
https://leetcode.com/problems/climbing-stairs/
 * @param {number} n
 * @return {number}
 */
let dp = {}
var climbStairs = function(n) {
    if(n > 2){
        let p1  = 1
        let p2  = 1
        let p3
        while(n -1){
            p3 = p1 + p2
            p2 = p1
            p1 = p3
            n--
        }
        return p3
    }
    if(n == 2){
        return 2
    }
    if(n ==1){
        return 1
    }
};