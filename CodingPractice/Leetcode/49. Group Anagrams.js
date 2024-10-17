/**
 // 49. Group Anagrams
 https://leetcode.com/problems/group-anagrams/
 * @param {string[]} strs
 * @return {string[][]}
 */
 var groupAnagrams = function(strs) {
    let map = {}
    strs.forEach( item =>{
        let word = item.split("").sort().join("")
        if(map[word]){
            map[word].push(item)
        }else{
            map[word] = [item]
        }
    })
    return Object.values(map)
};