/**
 * 415. Add Strings
 * https://leetcode.com/problems/add-strings/
 * @param {string} num1
 * @param {string} num2
 * @return {string}
 */
 var addStrings = function(num1, num2) {
    // num1 = num1.split("")
    // num2 = num2.split("")
    let [r1 , r2] = [num1.length -1, num2.length -1]
    let res = ""
    let prevSum = 0
    let carry = 0
    while( r1 >=0 && r2 >= 0 ){
        let asciSum = num1.charCodeAt(r1)  + num2.charCodeAt(r2) - 96 + carry
        console.log("ascii sum of ", num1[r1] , num2[r2] , asciSum)
        prevSum = asciSum
        let sum = asciSum %10
        carry = prevSum/10 | 0
        res = sum + res
        r1--
        r2--
    }
    while(r1 >= 0){
        let num = num1.charCodeAt(r1) + carry - 48
        let sum = num % 10
        carry = num/10 | 0
        res = sum + res
        // carry = 0
        r1--
    }
    while(r2 >= 0){
        let num = num2.charCodeAt(r2) + carry - 48
        let sum = num % 10
        carry = num/10 | 0
        res = sum + res
        r2--
    }
    console.log(carry)
    if( carry ){
        res = carry + res
    }
    console.log(res)
    return res
};