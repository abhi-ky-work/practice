/**
 * 54. Spiral Matrix
 * https://leetcode.com/problems/spiral-matrix/
 * @param {number[][]} matrix
 * @return {number[]}
 */
 var spiralOrder = function(matrix) {
    let res = []
    let left = 0
    let right = matrix[0].length 
    let top  = 0
    let bottom =  matrix.length
    // console.log( left, right, top, bottom)
    while( left < right && top < bottom){
        // left to right top most row
        for(let i = left ; i < right ; i++){
            res.push(matrix[top][i])
        }
        top++
        // top to bottom on right most col
        for(let i = top ; i < bottom ; i++ ){
            res.push(matrix[i][right -1])
        }
        right--
        // if we just finished single row or col
        if( ! ( left < right && top < bottom)){
            break
        } 
        // right to left on bottom most row
        for( let i = right -1 ; i >= left ; i--){
            res.push(matrix[bottom -1][i])
        }
        bottom--
        // bottom to top on left most
        for(let i = bottom -1 ; i >= top ; i--){
            res.push(matrix[i][left])
        }
        left++
        // console.log(top, right, bottom, left)
    }
    return res
};
