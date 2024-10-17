function waysToGetN(n){
    // using 1, 3, 4
    if( n === 0 || n === 1 || n === 2){
        return 1
    }
    else if( n === 3){
        return 2
    }
    let sum1 = waysToGetN(n - 1)
    let sum2 = waysToGetN(n - 3)
    let sum3 = waysToGetN(n - 4)
    return sum1 + sum2 + sum3
}
num = 4

console.log(waysToGetN(num))