"use strict";

const fs = require("fs");

const express = require("express");

const app = express();
const port = 5015;
app.listen(port);
console.log("My server on port " + port);

app.get("/me/page", function(request, response) {
    const nameString = request.query.p;
    if (fs.existsSync(nameString)) {
        const contentString = fs.readFileSync(nameString, "utf8");
        response.end(contentString);
    } else {
        const contentString = fs.readFileSync("bad.html", "utf8");
        response.end(contentString);
    }
});

app.get("/array", function(request, response) {
    const a = request.query.a;
    const b = request.query.b;
    const c = request.query.c;
    const aInt = parseInt(a);
    const bInt = parseInt(b);
    const cInt = parseInt(c);
    let arr = [];
    let n = bInt - aInt;
    for (let i = 0; i <= n; i++) {
        let tmp = aInt + i;
        if ( tmp % cInt == 0) {
            arr.push(tmp);
        }
    }
    const answerJSON = JSON.stringify({result: arr});
    response.end(answerJSON);
});