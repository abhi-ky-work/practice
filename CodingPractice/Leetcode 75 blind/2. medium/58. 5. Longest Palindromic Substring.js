/**
 * 5. Longest Palindromic Substring
 * https://leetcode.com/problems/longest-palindromic-substring/
 * @param {string} s
 * @return {string}
 */
 var longestPalindrome = function(s) {
    function searchPalindrome(s, l, r){
        let res = ""
        let resLen = 0 
        while( l >=0 && r < s.length && s[l] === s[r]){
            if( (r - l + 1) > resLen){
                resLen = r-l+1
                res = s.slice(l,r+1)
            }
            l--
            r++
        }
        return [res , resLen]
    }
    let result = ""
    let resultLen = 0
    for(let i = 0 ; i < s.length ; i++){
        let [resOdd, resOddLen ] = searchPalindrome(s, i, i )
        let [resEven, resEvenLen ] = searchPalindrome(s, i, i+1 )
        if(  resOddLen >= resultLen  ){
            resultLen = resOddLen
            result = resOdd
        }
        if(resEvenLen >= resultLen ){
            resultLen = resEvenLen
            result = resEven
        }
    }
    return result
};



/**
 * @param {string} s
 * @return {string}
 */
 var longestPalindrome = function(s) {
    let result = ""
    for(let i = 0 ; i < s.length ; i++){
        result = [
            result, 
            searchPalindrome(s, i, i ), 
            searchPalindrome(s, i, i+1 )
        ].reduce((res,str) => str.length > res.length ? str : res)
    }
    return result
};
function searchPalindrome(s, l, r){
    let res = ""
    let resLen = 0 
    while( l >=0 && r < s.length && s[l] === s[r]){
        let len = r - l + 1
        if( len > resLen){
            resLen = len
            res = s.slice(l,r+1)
        }
        l--
        r++
    }
    return res
}



// class Solution {
//     record Palindrome(String palindrome, int palindromeLength) {}

//     public Palindrome searchPalindrome(String s, int l, int r){
//         int strLength = 0;
//         String palindrome = "";
//         while(l >=0 && r < s.length() && s.charAt(l) == s.charAt(r)){
//             if( r - l + 1 > strLength){
//                 strLength = r - l + 1;
//                 palindrome = s.substring(l, r+1);
//             };
//             l--;
//             r++;
//         };
//         System.out.println("Interim Palindromes =>" + palindrome + " Length : " + strLength);

//         return new Palindrome(palindrome, strLength);

//     };


//     public String longestPalindrome(String s) {
//         String resPalindrome = "";
//         int resPalindromeLength = 0;

//         for(int i = 0 ; i < s.length() ; i++){
//             Palindrome oddStrPal = searchPalindrome(s, i, i);
//             Palindrome evenStrPal = searchPalindrome(s, i , i+1);

//             if( oddStrPal.palindromeLength >= resPalindromeLength ){
//                 resPalindrome = oddStrPal.palindrome;
//                 resPalindromeLength = oddStrPal.palindromeLength;
//             };
//             if( evenStrPal.palindromeLength >= resPalindromeLength ){
//                 resPalindrome = evenStrPal.palindrome;
//                 resPalindromeLength = evenStrPal.palindromeLength;
//             };
//         };
//         System.out.println("Anser Palindrome" + resPalindrome);
//         return resPalindrome;

//     }
// }