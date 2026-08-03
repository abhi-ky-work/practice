/**
 * 2. 3. Longest Substring Without Repeating Characters.js
 * https://leetcode.com/problems/longest-substring-without-repeating-characters/?envType=list&envId=xi4ci4ig
 * https://www.youtube.com/watch?v=wiGpQwVHdE0
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


// import java.util.HashSet;
// import java.util.Set;

// class Solution {
//     public int lengthOfLongestSubstring(String s) {
//         Set<Character> set = new HashSet();
//         int l = 0;
//         int res = 0;
//         for(int i = 0 ; i < s.length() ; i++){
//             while( set.contains(s.charAt(i))){
//                 set.remove(s.charAt(l));
//                 l++;
//             };
//             set.add(s.charAt(i));
//             res = Math.max(res, i - l + 1);
//         };
//         return res;
//     }
// }


// class Solution {
//     public int lengthOfLongestSubstring(String s) {
//         int charIndex[] = new int[128];

//         int maxLength=0, left=0;
        
//         for(int right = 0; right<s.length(); right++){
//             char ch = s.charAt(right);
//             left = Math.max(left, charIndex[ch]);

//             charIndex[ch] = right + 1;

//             maxLength = Math.max(maxLength,right - left + 1); 
//         }

//         return maxLength;
//     }
// }