// https://www.youtube.com/watch?v=92BfuxHn2XE

// select the min/max from unsorted and place at the right of sorted list
// tc n^2
// sc 1

arr = [1, 3, 5, 2, 55, 22, 12, 34 ,26 , 64 , 36 , 54 , 32 , 34 ]
// arr = [1, 3, 2 ]



for( i = 0 ; i< arr.length ; i++){
    min = i
    for( j = i+1; j < arr.length ; j++){
        if( arr[j] <  arr[i]){
            min = j
        }
    }
    // console.log(arr[min])
    if( min != i){
        temp = arr[min]
        arr[min] = arr[i]
        arr[i] = temp
        // [arr[min] , arr[i]] = [arr[i], arr[min]]
    }
}

console.log(arr)
// let a = 4
// let b = 5

// [a, b] = [b,a]
// console.log( a ," ",  b)