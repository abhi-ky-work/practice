// https://www.youtube.com/watch?v=Cq7SMsQBEUw
// in space and stable
// avg tc n^2
// sc 1

// in every iteration we get largest/smallest integer at last


arr = [1, 3, 5, 2, 55, 22, 12, 34 ,26 , 64 , 36 , 54 , 32 , 34 ]



for( let i = 0; i < arr.length ; i++){
    for( let j = 0 ; j < arr.length - i- 1 ; j++){
        if( arr[j] > arr[j+1]){
            temp = arr[j+1]
            arr[j+1] = arr[j]
            arr[j] = temp
        }
    }
}

console.log(arr)