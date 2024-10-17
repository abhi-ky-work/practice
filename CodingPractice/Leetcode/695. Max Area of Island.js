
/**
 * 695. Max Area of Island
 * https://leetcode.com/problems/max-area-of-island/
 * @param {number[][]} grid
 * @return {number}
 */
 var maxAreaOfIsland = function(grid) {
    let m = grid.length
    let n = grid[0].length
    let area = 0
    function dfs(i,j){
        if( i < 0 || i > m-1 || j < 0 || j > n-1 || grid[i][j] === 0) return 0
        grid[i][j] = 0

        return 1 + dfs(i, j -1) + dfs(i, j+1) + dfs(i-1, j) + dfs(i+1 , j)
    }
    for(let i = 0 ; i < m ; i++){
        for(let j = 0 ; j < n ; j++){
            area = Math.max(area, dfs(i,j))
        }
    }
    return area
};




/**
 * @param {number[][]} grid
 * @return {number}
 */
 var maxAreaOfIsland = function(grid) {
    if(grid){
    let m = grid.length
    let n = grid[0].length
    let area = 0
        for(let i = 0 ; i < m ; i++){
            for(let j = 0 ; j < n ; j++){
                if( grid[i][j] > 0 ){
                    area = Math.max(area , trace(i,j, m , n,grid))
                }
            }
        }
    return area
    }
};
function trace(i,j, m , n, grid){
    let dir = [[1,0],[-1,0],[0,1],[0,-1]]
    let q = [[i,j]]
    let l = 0
    let r = 0
    let area = 0
    grid[i][j] = 0
    while( l <= r){
        let _i = q[l][0]
        let _j = q[l][1]
        for(let d = 0 ; d < dir.length ; d++ ){
            let i2 = _i +dir[d][0]
            let j2 = _j +dir[d][1]
            if( i2 >=0 && i2 < m && j2 >= 0 && j2 < n && grid[i2][j2] === 1){
                q.push([i2,j2])
                grid[i2][j2] = 0
                r++
            }
        }
        l++
        area++
    }
    return area
}

let island = [
    [1,1,0,0,0],
    [1,1,0,0,0],
    [0,0,0,1,1],
    [0,0,0,1,1]]
console.log(maxAreaOfIsland(island) )

