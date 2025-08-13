/**
 * 2. 3. Longest Substring Without Repeating Characters.js
 * https://leetcode.com/problems/longest-substring-without-repeating-characters/?envType=list&envId=xi4ci4ig
 * @param {string} s
 * @return {number}
 */
 var lengthOfLongestSubstring = function(s) {
    
    let set = new Set()
    let l = 0
    let res = 0
    for(let i = 0; i < s.length ; i++){
        while( set.has(s[i])){
            set.delete(s[l])
            l++
        }
        set.add(s[i])
        res = Math.max(res, i-l +1)
    }
    return res
};