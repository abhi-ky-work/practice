/**
 * 1423. Maximum Points You Can Obtain from Cards
 * https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/
 * @param {number[]} cardPoints
 * @param {number} k
 * @return {number}
 */
 var maxScore = function(cardPoints, k) {
    
    let sum = 0
    let l= 0
    let r = cardPoints.length -k
    for(let i = r;i < cardPoints.length ; i++){
        sum += cardPoints[i]
    }
    let temp = sum
    for(let j = r ; j< cardPoints.length ; j++){
        sum = Math.max(sum, temp += cardPoints[l] - cardPoints[j])
        l++
    }
    return sum
};

// this didn't wokred
// /**
//  * @param {number[]} cardPoints
//  * @param {number} k
//  * @return {number}
//  */
//  var maxScore = function(cardPoints, k) {
    
//     let sum = find(0, 0 , k, cardPoints)
//     return sum
// };
// function find(sum, n, k , cardPoints){

//     if( n === k){
//         return sum
//     }
//     let sum1 = find(sum + cardPoints[n], n+1, k, [...cardPoints])
//     let sum2 = find( sum + cardPoints[cardPoints.length - 1 - n], n+1,k, cardPoints)
//     return Math.max(sum1,sum2)
// }