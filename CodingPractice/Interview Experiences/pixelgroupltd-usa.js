// nodejs buffers, react render dom functions, aws dynamodb, 
// return sum of fractions

/* 
num1/den1,num2/den2
input string : "1/500,2/500"
res :string  =  "3/500"

input string : "1/3,3/9"
res :string  =  "2/3"
*/

resNum = (num1 * den2 ) + ( num2 * den1)
resDen = den1 * den2
if( resNum % factors[i] == 0 && resDen % factors[i] == 0 ){
    resNum = resNum / factors[i]
    resDen = resDen / factors[i]
}

return resNum + "/" + resDen