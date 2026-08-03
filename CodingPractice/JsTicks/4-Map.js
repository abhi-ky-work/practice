let arr = new Map()

let a = [1,4,3,22,5,33,44,77,3,22, {name: "abhishek"}]
for(let item of a){
    arr.set(item, item + 5 )
}

arr.forEach( (val, key) =>{
    console.log( key, val)
    console.log("getting with key ", arr.get(key))
})

console.log(arr)
/* 
Map(9) {
  1 => 6,
  4 => 9,
  3 => 8,
  22 => 27,
  5 => 10,
  33 => 38,
  44 => 49,
  77 => 82,
  { name: 'abhishek' } => '[object Object]5'
}
 */
console.log(arr.size )          // 8
console.log(arr.get(33))        // 38
console.log(arr.has(33))        // true
console.log(arr.delete(33))     // true
console.log(arr.has(33))        // false
console.log(arr.values())       // [Map Iterator] { 6, 9, 8, 27, 10, 49, 82 }
console.log(arr.keys())         // [Map Iterator] { 1, 4, 3, 22, 5, 44, 77 }
console.log(arr.entries())      // [Map Entries] {
                                //   [ 1, 6 ],
                                //   [ 4, 9 ],
                                //   [ 3, 8 ],
                                //   [ 22, 27 ],
                                //   [ 5, 10 ],
                                //   [ 44, 49 ],
                                //   [ 77, 82 ]
                                // }
console.log(arr.delete(100))    // false











