"use strict";

const readlineSync = require('readline-sync');
const fs = require("fs");

const n = parseInt(readlineSync.question("Input count of file: "));
console.log(n);
let tmp = 0;

let str = '';

while(tmp !== n) {
    const file_name = readlineSync.question("Input file: ");
    if (fs.existsSync(file_name)) {
        str += fs.readFileSync(file_name, "utf8");
        tmp++;
    } else {
        console.log("File was not found");
    }
}

fs.writeFileSync("result.txt", str);
console.log("Create File OK");