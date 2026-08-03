let personName  = {
    firstName : "Abhishek",
    lastName  : "Yadav"
}


function printFullName(city, country){
    console.log(this.firstName + " " + this.lastName, "from : "+ city +", "+ country)   
}

// function.call(thisArg, arg1, arg2, ...)

printFullName.call(personName, "agra", "india")  // Call method


printFullName.apply(personName, ['Agra', "India"] ) // Apply method


let printBindedName = printFullName.bind(personName, "Agra", "India") // Bind method

printBindedName()