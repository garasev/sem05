"use strict";

const fs = require("fs");

const express = require("express");

const app = express();
const port = 5015;
app.listen(port);
console.log("My server on port " + port);

app.get("/me/page", function(request, response) {
    const nameString = "a.html";
    console.log(nameString);
    if (fs.existsSync(nameString)) {
        const contentString = fs.readFileSync(nameString, "utf8");
        response.end(contentString);
    } else {
        const contentString = fs.readFileSync("bad.html", "utf8");
        response.end(contentString);
    }
});

app.get("/input_fields", function(request, response) {
    let fields = request.query.fields;
    fields = fields.split(",");
    const adress = request.query.adress;
    const nameString = "result.html";
    let html_page = '<!DOCTYPE html>\n\
<html>\n\
<head>\n\
    <meta charset="UTF-8">\n\
    <title>Запросы</title>\n\
</head>\n\
<body>\n\
    <h1>Новая страница запроса</h1>\n\
    <form method="GET" action="/' + adress + '">\n'
    for (let field of fields){
        html_page += '        <p>' + field + '</p>\n';
        html_page += '        <input name="' + field + '" spellcheck="false" autocomplete="off">\n'
    }
    html_page += '        <br>\n\
        <br>\n\
        <input type="submit" value="Отправить запрос">\n\
    </form>\n\
</body>\n\
</html>'
    
    app.get("/" + adress, function(request, response) {
        let arr = request.query;
        let contentString = JSON.stringify(arr);
        response.end(contentString);
        
    });
    response.end(html_page);
});