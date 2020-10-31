"use strict";

// импортируем библиотеки
const express = require("express");
const cookieSession = require("cookie-session");
const fs = require("fs");

// запускаем сервер
const app = express();
const port = 5000;
app.listen(port);
console.log(`Server on port ${port}`);

const way = __dirname + "/static";  
app.use(express.static(way));

const users = [
    {"login" : "nikita", "password" : "1830", "age" : 20, "hobby" : "tennis"},
    {"login" : "dima", "password" : "da", "age" : 1, "hobby" : "peniboards"}
]

// работа с сессией
app.use(cookieSession({
    name: 'session',
    keys: ['hhh', 'qqq', 'vvv'],
    maxAge: 24 * 60 * 60 * 1000 * 365
}));

// заголовки в ответ клиенту
app.use(function(req, res, next) {
    res.header("Cache-Control", "no-cache, no-store, must-revalidate");
    res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
    next();
});

// сохранить cookie
app.get("/request", function(request, response) {
    // получаем параметры запроса
    const login = request.query.login;
    const password = request.query.password;

    
    let flagAuth = false;
    let answerString = "false";
    for (let i = 0; i < users.length; i++) {
        if (users[i].login === login && users[i].password === password) {
            flagAuth = true;
            break;
        }
    }
    if (flagAuth) {
        request.session.login = login;
        request.session.password = password;
        answerString = "true";
    }
    response.end(JSON.stringify({"answer" : answerString}));
});

app.get("/info", function(request, response) {
    // получаем параметры запроса
    const login = request.session.login
    const password = request.session.password

    for (let i = 0; i < users.length; i++) {
        if (users[i].login === login && users[i].password === password)
            response.end(JSON.stringify(users[i]))
    }
});

// получить cookie
app.get("/api/get", function(request, response) {
    // контролируем существование cookie
    if(!request.session.login) return response.end("Not exists");
    if(!request.session.age) return response.end("Not exists");
    // отправляем ответ с содержимым cookie
    const login = request.session.login;
    const age = request.session.age;
    response.end(JSON.stringify({
        login,
        age
    }));
});

// удалить все cookie
app.get("/api/delete", function(request, response) {
    request.session = null;
    response.end("Delete cookie ok");
});

