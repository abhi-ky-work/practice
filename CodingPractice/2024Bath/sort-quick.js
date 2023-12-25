// tc nlog(n)
// sc 1


array = [1, 3, 5, 2, 55, 22, 12, 34 ,26 , 64 , 36 , 54 , 32 , 34 ]



function quickSort(arr, p , q){
    
    if (p<q ){
        m = partition(arr, p, q)
        quickSort( arr , p , m -1 )
        quickSort( arr, m + 1 , q)

    }
}
function partition(arr, p, q){
    let pivot = arr[q-1]
    let i = p - 1
    let j = p

    for( j = p ; j < q  ; j++){

        if( arr[j] <= pivot ){
            i++
            let temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
        }
    }
    return i
}



quickSort(array, 0 , array.length )
console.log("Result => ", array)