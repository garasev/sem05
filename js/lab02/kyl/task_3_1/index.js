"use strict";

let tmp = 0;

let arr = [];
let str;

const readlineSync = require('readline-sync');

const n = parseInt(readlineSync.question("Input count of string: "));

while(tmp !== n) {
    str = readlineSync.question("Input string: ");
    if (str.length % 2 ==  0) {
         arr.push(str);
    }
    tmp++;
}

const fs = require("fs");

const nameString = "task31.txt";

const contentString = JSON.stringify(arr);
fs.writeFileSync(nameString, contentString);

console.log("Create File OK");