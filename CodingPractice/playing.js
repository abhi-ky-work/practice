let s = 'ameewmea' // 6
// let s = 'elrmenmet' # 5


function longestPalindromicSubsequence(s, l, r){

    if( l > r) return 0
    if(r === l ) return 1
    let c1 = 0
    if( s[l] === s[r] && l < r){
        c1 = 2 + longestPalindromicSubsequence(s, l+1 , r-1)
    }
    let c2 = longestPalindromicSubsequence(s, l+1, r)
    let c3 = longestPalindromicSubsequence(s, l, r-1)

    return Math.max(c1, c2, c3)

}

console.log(longestPalindromicSubsequence(s, 0 , s.length -1))