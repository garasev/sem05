"use strict";

// импортируем библиотеку
const express = require("express");
const fs = require("fs");

// запускаем сервер
const app = express();
const port = 5000;
app.listen(port);
console.log(`Server on port ${port}`);

// отправка статических файлов
const way = __dirname + "/static";
app.use(express.static(way));

// заголовки в ответ клиенту
app.use(function(req, res, next) {
    res.header("Cache-Control", "no-cache, no-store, must-revalidate");
    res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
    res.header("Access-Control-Allow-Origin", "*");
    next();
});

// body
function loadBody(request, callback) {
    let body = [];
    request.on('data', (chunk) => {
        body.push(chunk);
    }).on('end', () => {
        body = Buffer.concat(body).toString();
        callback(body);
    });
}

function checkUniqe(obj, mail, phone) {
    for (let i = 0; i < obj.length; i++) {
        if (obj[i].mail === mail || obj[i].phone === phone) {
            return false;
        }
    }
    return true;
}

// it is post
app.post("/save/info", function(request, response) {
    loadBody(request, function(body) {
        const obj = JSON.parse(body);
        const mail = obj["mail"];
        const surname = obj["surname"];
        const phone = obj["phone"]; 

        let contentString = fs.readFileSync("./file.txt", "utf8");
        let answerString = "Не добавили человека";
        if (mail === '' || surname === '' || phone === '') {
            answerString = "Заполните поля";
        } else {
            let obj;
            if (contentString === '') {
                obj = []; 
            } else {
                obj = JSON.parse(contentString);
            }
            if (checkUniqe(obj, mail, phone)) {
                obj.push({"mail": mail, "surname": surname, "phone":phone})
                contentString = JSON.stringify(obj);
                fs.writeFileSync("./file.txt", contentString);
                answerString = "Добавили человека"
            }
        }
        response.end(JSON.stringify({
            answer: answerString,
            curFile: contentString
        }));
    });
});