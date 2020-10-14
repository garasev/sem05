"use strict";

function recursionReadFile(dir) {
    const arr = fs.readdirSync(dir);
    for (let i = 0; i < arr.length; i++) {
        try {
            const fileText = fs.readFileSync(dir + arr[i], "utf8");
            if (fileText.length <= 10) {
                console.log(fileText);
            }
        } catch(err) {
            recursionReadFile(dir + arr[i] + '/');
        }
    }
}

const fs = require("fs");
const dir = "./1/"
recursionReadFile(dir);
