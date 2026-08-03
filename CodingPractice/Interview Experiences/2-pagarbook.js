// given array of 0 , positive intergers and -ve integers 
// return array with positive intergers first retaining the order and the 0's in the end 
// Input: 1 ,0 ,2 ,3 ,0 ,4 ,0 ,1
// Output: 1 ,2 ,3 ,4 ,1 ,0 ,0 ,0
// 1 ,2 ,0 ,3 ,0 ,4 ,0 ,1
// 1 ,2 ,3 ,0 ,0 ,4 ,0 ,1
// 1 ,2 ,3 ,0 ,0 ,4 ,0 ,1
// 1 ,2 ,3 ,4 ,0 ,0 ,0 ,1
// 1 ,2 ,3 ,4 ,1 ,0 ,0 ,0




arr=[1,0, 2, 3, 0,4,0,1]
p = 0 
z = 0 

/* for(let i = 0 ; i < arr.length ; i++ ){
    if(arr[i] != 0){
        arr[p] = arr[i]
        p++
    }
}

while(p < arr.length){
    arr[p] = 0
    p++
}

console.log(arr) */


for(let i in 100){
    console.log(i)
}