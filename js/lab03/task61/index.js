"use strict";

// импорт библиотеки
const express = require("express");

// запускаем сервер
const app = express();
const port = 5000;
app.listen(port);
console.log(`Server on port ${port}`);

// активируем шаблонизатор
app.set("view engine", "hbs");

// заголовки в ответ клиенту
app.use(function(req, res, next) {
    res.header("Cache-Control", "no-cache, no-store, must-revalidate");
    res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
    res.header("Access-Control-Allow-Origin", "*");
    next();
});

let gameArray = [
    {name: "DOTA2", description: "multiplayer online battle arena", age: 6},
    {name: "GTA5", description: "action-adventure", age: 18},
    {name: "CS-GO", description: "first-person shooter", age: 16}
];

// выдача страницы c играми
app.get("/page/games", function(request, response) {
    const key = request.query.k;
    console.log(key);
    const infoObject = {
        descriptionValue: `Список компьютерных игр, с возрастным ограничением ${key}`,
        games : gameArray.filter(obj => obj.age <= key)
    };
    response.render("pageGames.hbs", infoObject);
});