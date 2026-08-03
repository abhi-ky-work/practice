
var firstObj = {
  val1 : 1,
  val2 : {
    val3: 4,
    val4: {
        val5: "Stringvalue"
    }
  }
};


var secondObj = {
  val1 : 1,
  val2 : {
    val3: 4,
    val4: {
        val5: "Stringvalue"
    }
  }
};



var a = {random:'1'};
var b = {random:'1'};
var c = a;

function isSame(a, b){
    console.log(a == b)
}
isSame(a,b)

// isSame(firstObj,secondObj) => true : false


 
// console.log(a.d.a.b1); // 1
// console.log(b.d.a.b1); // hello


// 

let a = {    a: 1,
    b: {
        b1: 2,
        b2: {
            b21: 3,
            b22: "hello"
        }
    },
    c: 4
}
function sum (obj){
    let val = Object.values(obj)
    let sum = 0
    
    val.forEach(item =>{
        if( typeof(item) == "number" ){
             sum += item
        }
        sum(item, sum)
    })
    return sum
}
// sum(a)
sum(a)

function x(){
    let executed = false
    return ()=>{
        if( !executed){
            console.log("hello")
            executed = true
        }
    }
}

let run = x()

// run();
 // run();




