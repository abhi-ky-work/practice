// https://www.youtube.com/watch?v=8oJS1BMKE64

// tc n^2
// sc 1



arr = [1, 3, 5, 2, 55, 22, 12, 34 ,26 , 64 , 36 , 54 , 32 , 34 ]


for( i = 0 ; i < arr.length ; i++){
    j = i
    currNum = arr[i]
    while ( j > 0 && currNum < arr[j-1] ){
        arr[j] = arr[j-1]
        j--
    }
    arr[j] = currNum
}
console.log( arr )