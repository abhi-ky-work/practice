/**
 * 1169. Invalid Transactions
 * https://leetcode.com/problems/invalid-transactions/
 * @param {string[]} transactions
 * @return {string[]}
 */
 var invalidTransactions = function(transactions ) {
    let res = {}
    let map = {}
    for(let i = 0 ; i< transactions.length ; i++){
        let item = transactions[i]
        let [userName,time,amt,city] = item.split(",")
        if(amt > 1000 ){
            res[i] = item
        }
        if( map[userName]){
            map[userName].forEach( t =>{
            let [time2, city2, index ] = t.split(',')
                if(city != city2 && Math.abs(time2 - time) <= 60){
                    res[i] = item
                    res[index] = transactions[index]
                }
            })
            map[userName].push(time+","+city+","+i)
        }else{
            map[userName] = [time+","+city+","+i]
        }
    }
    return Object.values(res)
};

/**
 * https://leetcode.com/problems/invalid-transactions/
 * @param {string[]} transactions
 * @return {string[]}
 */
 var invalidTransactions = function(transactions ) {
    let invalidTransactions = []
    let parsedTransactions = transactions.map(item =>{
        let [name, time, amt , city]= item.split(",")
        return { name, time : parseInt(time), amt : parseInt(amt), city }
    })
    parsedTransactions.forEach((item, index) =>{
        if( item.amt > 1000){
            invalidTransactions.push(transactions[index])
        }else{
            let isInvalid = parsedTransactions.some( ot =>ot.name == item.name &&
                ot.city != item.city &&
                Math.abs( ot.time - item.time) <= 60)
            if( isInvalid ){
                invalidTransactions.push(transactions[index])
            }
        }
    })
    return invalidTransactions
};