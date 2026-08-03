// write the programm to return the array sorted by maximum frequency of elements
// if the freq is same keep the smaller number before
// [4,5,6,5,4,3] => [4,4,5,5,6,3]


// write the programm to return the array sorted by maximum frequency of elements
// if the freq is same keep the smaller number before
// [4,5,6,5,4,3] => [4,4,5,5,6,3]


function maxFrequencySort(arr){
    let freq = {}
    for(let item of arr){
       freq[item] = ( freq[item] +1 || 1 )
    }
    console.log(freq)
    arr.sort( (a,b) => {
        if( freq[a] === freq[b]){
            return a - b
        }
        return freq[b] - freq[a]
    })

    console.log(arr)

}

maxFrequencySort([4,5,6,5,4,3])
















/* 
function maxFrequencySort(arr){
    let freq = new Map()
    for(let item of arr){
        if(freq.has(item)){
            freq.set(item, freq.get(item) + 1) 
        }else{
            freq.set(item, 1) 
        }
    }
    arr.sort( (a,b) => {
        if( freq.get(a) === freq.get(b)){
            return a - b
        }
        return freq.get(b) - freq.get(a)
    })

    console.log(arr)

}

let arr = [4,5,6,5,4,3]
maxFrequencySort(arr) */