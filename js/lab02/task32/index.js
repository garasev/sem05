"use strict";

function checkOnlyVowels(str) {
    let vowel = ['A', 'E', 'U', 'Y', 'I', 'O'];
    let tmp_str = str.toUpperCase();
    for (let i = 0; i < tmp_str.length; i++) {
        if (vowel.indexOf(tmp_str[i]) == -1) {
            return false;
        }
    }
    return true;
}


const fs = require("fs");

const nameString = "task32.txt";

if (fs.existsSync(nameString)) {
    const contentString = fs.readFileSync(nameString, "utf8");
    const obj = JSON.parse(contentString);
    for(let i = 0; i < obj.length; i++) {
        if (checkOnlyVowels(obj[i])) {
            console.log(obj[i]);
        }
    }
} else {
    console.log("File was not found");
}