"use strict";

window.onload = function() {
    const name_input = document.getElementById("name_input");
    const price_input = document.getElementById("price_input");

    const btn = document.getElementById("add_btn");
    const label = document.getElementById("result_label");

    function ajaxGet(urlString, callback) {
        let request = new XMLHttpRequest();
        request.open("POST", urlString, true);
        request.setRequestHeader("Content-Type", "text/plain;charset=UTF-8");
        request.send(null);
        request.onload = function() {
            callback(request.response);
        };
    };

    btn.onclick = function() {
        const name = name_input.value;
        const price = price_input.value;

        const url = `/add_car?name=${name}&price=${price}`;
        ajaxGet(url, function(stringAnswer) {
            const objectAnswer = JSON.parse(stringAnswer);
            const added = objectAnswer.answer;
            label.innerHTML = added ? `Машина <font color="red">${name}</font> с ценой <font color="green">${price}</font> добавлена!` :
                                      `Машина <font color="red">${name}</font> уже существует в базе!`;                       
            });    
    };
};