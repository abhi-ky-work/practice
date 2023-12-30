// tc = o(NlogN) with quickSort , the efficient alog used for sorting the bucket
// sc = o(1)     with quicksort

arr = [30,63,10,12,20,45,99,22,50,60,40]


function bucketSort(arr){
    // max for cal of bucket index
    max = arr[0]
    // to get num of bucket 
    size = arr.length
    
    arr.forEach(el => {
        if(el > max){
            max = el
        }
    });
    // num of buckets
    numOfBuckets = (Math.sqrt(arr.length) )| 0

    buckets = Array.from(new Array(numOfBuckets), () => [])
    // putting element in bucket
    arr.forEach( item =>{
        bucketIndex = Math.ceil(( item * numOfBuckets)/max )
        buckets[bucketIndex-1].push(item)
    })
    arrayIndex = 0
    buckets.forEach( (bucket, index) =>{
        sortedBucket = quickSort(bucket, 0, bucket.length)
        sortedBucket.forEach( el =>{
            arr[arrayIndex ] = el
            arrayIndex ++
        })
    })
    
    
}

function quickSort( arr, p , q){
    if (p < q) {
        r = partition(arr, p, q)
        quickSort(arr, p , r - 1)
        quickSort(arr, r+1, p)
    }
    return arr
}
function partition(arr, p, q){
    let pivot = arr[q -1]

    let i = p -1
    let j = p
    for( j = p ; j < q; j++){
        if( arr[j] <= pivot){
            i++
            let temp = arr[j]
            arr[i] = arr[j]
            arr[j] = temp
            
        }
    }
    return i
}

bucketSort(arr)
console.log("REsult : ", arr)
