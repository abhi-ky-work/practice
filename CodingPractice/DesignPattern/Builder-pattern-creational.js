
function Person(name, gender, weight , height ){
    this.name = name
    this.gender=  gender
    this.weight= weight
    this.height= height


}

function PersonBuilder (name , gender){

    this.name = name
    this.gender = gender 

    this.setWeight = function (weight){
        this.weight = weight 
        return this
    }
    this.setheight = function ( height){
        this.height = height 
        return this
    }
    this.build = function(){
        return new Person(this.name , this.gender, this.weight , this.height)
    }
}

let avinash = new PersonBuilder("avinash", "male").setWeight(33).setheight(3.4).build()
console.log(avinash)