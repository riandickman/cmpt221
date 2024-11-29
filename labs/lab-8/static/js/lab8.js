/****************************************************************************************************************/
/* In-Class Exercises                                                                                           */
/****************************************************************************************************************/
/* 1. create an array called "fruits" and assign the values "Strawberry", "Raspberry", and "Apple" to it         */
let fruits = [];
fruits = ["Strawberry", "Raspberry", "Apple"];

console.log(fruits)


/* 2. add two more fruits to the "fruits" array using the correct array method                                   */
fruits.push("Kiwi", "Mango");
console.log(fruits)

/* 3. sort the fruits array alphabetically using the correct array method                                        */
console.log(fruits.sort());

/* 4. create a function called printFruit that prints each item in the fruits array to the console              */
/*    and call the printFruit function                                                                          */
function printFruit() {
    for (let index in fruits) {
        console.log(fruits[index]);
    }}

printFruit();

class Fruit {
        constructor(name, color, season) {
        this.name = name,
        this.color = color,
        this.season = season
}
    printFruit() {
        console.log(
            "Fruit Name: " + this.name + ", Fruit Color: " + this.color +  ", Fruit Season: " + this.season
        );
    }
}

const strawberry = new Fruit("strawberry", "red", "Summer")
const apple = new Fruit("apple", "green", "Fall")
const pomegranate = new Fruit("pomegranate", "pink", "Winter")

strawberry.printFruit();
apple.printFruit();
pomegranate.printFruit();


/* 5. create a fruit class that has three properties: name, color, and season and one method: printFruit()      */
/*    that prints all three properties of the fruit to the console. Then, create 3 fruit objects and print      */
/*    them using the printFruit() method 

see above i dont know why this is comment GRRRRR





/****************************************************************************************************************/
/* In-Class Lab                                                                                                 */
/****************************************************************************************************************/
/* 1. Write a function that asks the user if they want to say hi. If the user selects "Okay" (true), then       */
/*    display a welcome message. If the user selects "Cancel" (false), then display a different message         */
function areYouSure() {
    let text = "Do you want to say hi?"
    if (confirm(text) === true) {
        text = "Welcome to Lab 8!";
    } else {
        text = "Rude!"
    }
    document.getElementById("example").innerHTML = text;
}

/* 2. Write a function to change 3 styles on the webpage                                                        */
function changeStyle() {
    document.body.style.backgroundColor = "hotpink"

    const buttons = document.querySelectorAll("button");
    buttons.forEach(button => {
    button.style.backgroundColor = "blue";
    button.style.color = "orange"
    });

}
