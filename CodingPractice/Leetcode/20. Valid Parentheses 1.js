/**
20. Valid Parentheses
https://leetcode.com/problems/valid-parentheses/?envType=problem-list-v2&envId=psz78mq6&favoriteSlug=&difficulty=EASY
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    let str = s.split("")
    let map = {
        "a" : 0,
        "b" : 0,
        "c" : 0
    }
    console.log(str)
    let validString = true
    let lastOpen = []
    if( validOpen(str[0]) ){
        lastOpen.push(str[0])
    }else return false
    for(let i = 0 ; i < str.length ; i++){
        if( validOpen( str[i]) ){
            map[validOpen( str[i])] += 1
            lastOpen.push(str[i])
        }else{
            if( validClose(str[i]) && map[validClose(str[i])] > 0  ){
                let lastItem = lastOpen.pop()
                console.log("lastItem : ", lastItem, " , current ", str[i])
                if(str[i] == getPair(lastItem)){
                    map[validClose( str[i])] -= 1
                }

            }
            else {
                validString = false
            }
        }
        console.log( str[i] , " : ", map)
    }
    if( map.a == 0 && map.b == 0 && map.c == 0 && validString){
        return true
    }else return false
};

var validOpen = (a)=>{

    if( a == "("  ){
        return "a"
    }
    if( a == "{"  ){
        return "b"
    }
    if( a == "["  ){
        return "c"
    }
    return false
}
var validClose = (a)=>{

    if( a == ")"  ){
        return "a"
    }
    if( a == "}"  ){
        return "b"
    }
    if( a == "]"  ){
        return "c"
    }
    return false
}

var getPair = (a)=>{

    if( a == "("  ){
        return ")"
    }
    if( a == "{"  ){
        return "}"
    }
    if( a == "["  ){
        return "]"
    }
    return "-"
}