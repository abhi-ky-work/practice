array = [22, 12,  55, 64 , 36 ,34 ,26 ,1, 3, 5, 2, 54 , 32 , 34 ]
// index = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

shift = 0

function shellSort(arr){

    let gap = arr.length / 2 | 0

    while( gap >0){
        // console.log("Gap :================ ", gap)
        // console.log(arr.join("-"))
        for( i = gap ; i < arr.length ; i++){
            let j = i
            // console.log("I ====>: ", i, arr[i])
            while (j >= gap && arr[j] < arr[j - gap]){
                // console.log("while : j swap : ", j , "and ", j-gap," ", arr[j-gap], " <> ",arr[j])
                temp = arr[j]
                arr[j] = arr[j-gap]
                arr[j-gap] = temp
                j = j - gap
                // console.log("while : j updated : ", j)
                // console.log("while : ", arr.join("-"))
                shift++
            }

        }
        gap = gap / 2 | 0 
    }
}


shellSort(array)
console.log(array)
console.log("shifts : ", shift)