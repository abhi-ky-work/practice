function getUnexpiredTokens (time_to_live, queries) {
    // Write your code here
    const tokenExpMap = {}
    const result = []
    
    for (let i = 0; i < queries.length ; i++){
        const query = queries[i].split(" ")
        let command = query[0]
        let tokenName
        let time
        
        if (command == "count") {
            //count queries handling
            let unExpiredCount = 0
            time = parseInt(query[1])
            Object.values(tokenExpMap).forEach(val =>{
                // if(val <= time || val == -1) unExpiredCount++
                if(val > time ) unExpiredCount++

            })
            result.push(unExpiredCount)
        } else {
            // generate and renew handling
            command = query[0]
            tokenName = query[1]
            time = parseInt(query[2])
            if(command == "generate"){
                tokenExpMap[tokenName] = time + time_to_live
            } else if(command == "renew"){
                if(tokenExpMap[tokenName] > time){
                    tokenExpMap[tokenName] = time + time_to_live
                }
            }
        }
    }
    return result
}
// time_to_live = 35
// queries = ["generate tokenl 3", "count 4", "generate token2 6", "count 7", "generate token 11", "count 41"]
// ans [1,2,1]

time_to_live = 5
queries = ["generate aaa 1", "renew aaa 2", "count 6", "generate bbb 7", "renew aaa 8", "renew bbb 10", "count 15"]
//ans [1,0]

console.log(getUnexpiredTokens(time_to_live, queries))






