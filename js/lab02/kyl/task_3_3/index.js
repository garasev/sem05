"use strict";

function checkExtension(extension, needCheckExtension) {
    for (let i = 0; i < extension.length; i++) {
        if (extension[extension.length - 1 - i] != needCheckExtension[needCheckExtension.length - 1 - i]) {
            return false;
        }
    }
    return true;
}

const fs = require("fs");
const readlineSync = require('readline-sync');


const extension = readlineSync.question("Input file extension with . : ")
const folder = readlineSync.question("Input adress folder: ")
const arr = fs.readdirSync(folder);

let readData = '';

for (let i = 0; i < arr.length; i++) {
    const fileName = folder + arr[i];
    if (checkExtension(extension, arr[i])) {
        const contentString = fs.readFileSync(fileName, "utf8");
        readData += contentString;
    }
}
console.log(readData);
