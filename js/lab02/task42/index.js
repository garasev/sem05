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
 
app.get("/getelem", function(request, response) {
    const index = parseInt(request.query.index);

    let res = JSON.parse(fs.readFileSync("arr.txt", "utf-8"));

    if (index < 0 || index >= res.length)
        response.end('Wrong index');
    const result = JSON.stringify(res[index]);
    response.end(result);
});