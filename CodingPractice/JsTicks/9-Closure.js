

function x(){
    var a = 10;
    return function y(){
        console.log(a);
    }
}

var z = x();
z();



// 



function x(){
    var a = 10;
    return () => console.log(a);
}

var z = x();
z();