var a = {random:'1'};
var b = {random:'1'};
var c = a;

function isSame(a, b){
    console.log(a === b)
}
isSame(a,b)
isSame(a,c)


