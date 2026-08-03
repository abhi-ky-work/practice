//  *
// ***
//*****
// r=3

// spaces = 
function print(r){
    function getChar(s, c){
        let str = ''
        for(let i = 0 ; i < s ; i++){
            str += c
        }
        return str
    }
    for(let i=1; i <=r ; i++){
        console.log(getChar(r-(i) , " ") + getChar( 2*i - 1, "*"))
    }
}

print(3)




