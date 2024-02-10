arr = [5,3,5,2,7,9,0,2,9,7]

res  = 0
// console.log(Math.abs(res))
for(let i = 1 ; i <= arr.length ; i++){
    res = res ^ arr[i-1]
    console.log(arr[i-1], " : ", res)
    // console.log(res)
}
console.log("ans : ",res)



