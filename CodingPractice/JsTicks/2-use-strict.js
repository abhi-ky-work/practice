


// - Assigning to undeclared variables
/* 
"use strict";
let mistypeVariable;

// Assuming no global variable mistypeVarible exists
// this line throws a ReferenceError due to the
// misspelling of "mistypeVariable" (lack of an "a")
mistypeVarible = 17;

 */


//  - Failing to assign to object properties

/* 
"use strict";

// Assignment to a non-writable global
// undefined = 5; // TypeError TypeError: Cannot assign to read only property 'undefined' of object '#<Object>'
// Infinity = 5; // TypeError

// // Assignment to a non-writable property
// const obj1 = {};
// Object.defineProperty(obj1, "x", { value: 42, writable: false });
// obj1.x = 9; // TypeError TypeError: Cannot assign to read only property 'x' of object '#<Object>'

// // Assignment to a getter-only property
// const obj2 = {
//   get x() {
//     return 17;
//   },
// };
// obj2.x = 5; // TypeError TypeError: Cannot set property x of #<Object> which has only a getter

// Assignment to a new property on a non-extensible object
// const fixed = {};
// Object.preventExtensions(fixed);
// fixed.newProp = "ohai"; // TypeError TypeError: Cannot add property newProp, object is not extensible

 */

/* 
function duplicateArguments(name, name , age){
    console.log(name , name , age)
}

duplicateArguments("Abhishek", "Ankitha", 34)



function duplicateArguments(name, name , age){
    "use strict"
    console.log(name , name , age)
}
console.log("After Use Strict => ")
duplicateArguments("Abhishek", "Ankitha", 34) */


// - Setting properties on primitive values
/* 

// false.true = ""


"use strict";

false.true = ""; // TypeError
(14).sailing = "home"; // TypeError
"with".you = "far away"; // TypeError */


// - Duplicate property names
/* 
"use strict";
const o = { p: 1, p: 2 }; // syntax error prior to ECMAScript 2015
console.log(o.p)

 */

// - Legacy octal literals
// Strict mode forbids a 0-prefixed octal literal or octal escape sequence. 
// In sloppy mode, a number beginning with a 0, such as 0644, is interpreted as an octal number (0644 === 420), 
// if all digits are smaller than 8. Novice developers sometimes believe a leading-zero prefix has no semantic meaning, 
// so they might use it as an alignment device — but this changes the number's meaning! 
// A leading-zero syntax for the octal is rarely useful and can be mistakenly used, so strict mode makes it a syntax error:

console.log(0644 === 420) // true
console.log(0644 == 420) // true
console.log(0644 == 644) // false
console.log(0644 === 644) // false
console.log(0644 == 0644) // true
console.log(644 == 644) // true
console.log(0684 === 684) // true
