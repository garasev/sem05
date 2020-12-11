"use strict";

function factorial(n) {
    return n ? n * factorial(n - 1) : 1;
}

let number = process.argv[2];
number = number.split(",");
let result = "";
for (let i = 0; i < number.length; i++) {
    number[i] = factorial(parseInt(number[i]));
    result += number[i] + " ";
}
console.log(result);