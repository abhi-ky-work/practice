// tc = o(N+K)
// sc = K = max-min + 1



array = [22, 12,  55, 64 , 36 ,34 ,26 ,1, -3, 5, 2, 54 , 32 , 34 ]

function countSort(arr){

    let min = arr[0]
    let max = arr[0]

    arr.forEach( item =>{
        if( item > max ){
            max = item
        }
        if( item < min){
            min = item
        }
    })
    // console.log( min , max)
    let countArray = Array(max-min +1).fill(0)
    
    arr.forEach( (item ) =>{
        countArray[item - min] += 1
    
    })
    // console.log(countArray)

    arrayIndex = 0

    countArray.forEach( ( item , index )=>{
        // console.log( item > 0 )
        while ( item > 0 ){
            arr[arrayIndex] = index + min
            arrayIndex ++
            item--
        }
    })

    // for( let i = min ; i < max + 1 ; i++){

    //     while ( countArray[ i - min] > 0 ){
    //         arr[arrayIndex] = i 
    //         arrayIndex ++
    //         countArray[ i - min] -= 1
    //     }
    // }
}

countSort(array)
console.log(array)