let a = {    
    a: 1,
    b: {
        b1: [1,2],
        b2: {
            b21: 3,
            b22: "hello"
        }
    },
    c: 4
}
console.log(deepSum(a))

function sumNumbers(obj) {
  let total = 0;

  for (let key in obj) {
    const value = obj[key];
    console.log(key , " : ", typeof value )
    if (typeof value === 'number') {
      total += value;
    } else if (Array.isArray(value)) {
      
    } else if (typeof value === 'object' && value !== null) {
      // recursively sum nested objects
      total += sumNumbers(value);
    }
  }

  return total;
}

// Example
let result = sumNumbers(a);
console.log(result);




// why this give 11
/* function deepSum(obj){
    let sum = 0
    for( let key in obj){
        let val = obj[key]
        let typ = typeof obj[key]

        if( typ === 'number'){
            sum += val
        }
        else if(typ === Array.isArray(val)){

        }else if( typ === 'object' && val !== null){
            sum += deepSum(val)
        }
    }

    return sum
} */