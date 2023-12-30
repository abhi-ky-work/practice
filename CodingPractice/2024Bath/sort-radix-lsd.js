// tc = o(N)
// sc = o(N)


arr = [30,63,1022,121,0,5,999,2,500,6110,40]

max = 0
arr.forEach(el => {
    len = (""+el).length
    if(len > max ){
        max = len
    }
});



bucket =Array.from( new Array(10), () => [])
// bucket[0].push(1)
// function radixSort(arr){
//     bucket = Array(10).fill([])
// }

// fill buckets
for( let i = 0 ; i< max ; i++){
    console.log("Iteration no =======> ", i)
    arr.forEach( item =>{
        let digit = ((item / Math.pow(10,i)) | 0) % 10
        // console.log(digit)
        bucket[digit].push(item)
        // console.log(bucket)
    })
    console.log("Bucket in iteration ========> ", i, " ; ", bucket)
    arrIndex = 0
    bucket.forEach( (item, index) =>{
        // code 1
        let itemIndex = 0
        while( itemIndex < item.length ){
           arr[arrIndex] = item[itemIndex]
           itemIndex++
           arrIndex++
        }
        bucket[index] = []
        // code 2
        // item = []
        // item.forEach( num =>{
        //     arr[arrIndex] = num
        //     arrIndex++
        // })
        // bucket[index] = []
    })
    console.log("arr after iteration ======= >  ", i , " : ", arr)
}

console.log(max)
console.log(bucket)
console.log("Result :", arr)