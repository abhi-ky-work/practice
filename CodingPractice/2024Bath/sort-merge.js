


arr = [1, 3, 5, 2, 55, 22, 12, 34 ,26 , 64 , 36 , 54 , 32 , 34 ]



function mergeSort(arr ){
    let arrLength = arr.length
    if( arrLength == 1){
        return
    }
    let m = arrLength / 2 | 0
    let leftArray = arr.slice(0, m)
    let rightArray = arr.slice(m)

    mergeSort(leftArray)
    mergeSort(rightArray)

    let i = 0
    let j = 0
    let k = 0

    while( i < leftArray.length && j < rightArray.length){
        if( leftArray[i] < rightArray[j]){
            arr[k] = leftArray[i]
            i++
        }else{
            arr[k] = rightArray[j]
            j++
        }
        k++
        
    }
    while ( i < leftArray.length){
        arr[k] = leftArray[i]
        k++ 
        i++
    }
    while( j < rightArray.length){
        arr[k] = rightArray[j]
        k++
        j++
    }

}

console.log(arr)

mergeSort(arr)
console.log(arr)