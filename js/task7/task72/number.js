"use strict";

function factorial(n) {
    return n ? n * factorial(n - 1) : 1;
}

const number = "" + process.argv[2];
const result = factorial(parseInt(number));
console.log("" + result);