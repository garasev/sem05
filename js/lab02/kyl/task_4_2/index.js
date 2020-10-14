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
 
app.get("/index/mas", function(request, response) {
    const index = request.query.index;
    const indInt = parseInt(index);
    let res = fs.readFileSync("test.txt", "utf-8");
    res = JSON.parse(res);
    if (indInt < 0 || indInt >= res.length)
        response.end('Wrong index');
    const resind = JSON.stringify(res[indInt]);
    response.end(resind);
});