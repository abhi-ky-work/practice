let aa = {    a: 1,
    b: {
        b1: 2,
        b2: {
            b21: 3,
            b22: "hello"
        }
    },
    c: 4
}




bb = {...aa} 
bb.a = 11

console.log(aa.a) // 1
console.log(bb.a) // 11



bb.b.b2.b22 = "world"

console.log(aa.b.b2.b22); // world
console.log(bb.b.b2.b22); // world