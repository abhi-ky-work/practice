let original = {    
    age: 25,
    name : { first : "John", last: "Doe" }
} 


let nextObj = JSON.parse(JSON.stringify(original))

nextObj.age = 30
nextObj.name.first = "Jane"

console.log(original.age) // 25
console.log(nextObj.age) // 30




// 

let data1 = { a : 1 , b : { c : 2 } }

let data2 = { ...data1 }


console.log( data1.b.c ) // rectify the code to print 3 

data2.b.c = 3

console.log( data1.b.c ) // 3