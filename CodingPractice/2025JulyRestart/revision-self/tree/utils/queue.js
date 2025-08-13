const queue = []
const size = 0
const top = 0

function insert(item){
    queue.push(item)
    size++
    console.log("Added to queue : ", queue)
}

function peek(){
    return queue[0]
}

function pop(){
    let item = queue.shift()
    console.log("Removed form queue : ", item)
    return item
}

