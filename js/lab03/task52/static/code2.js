"use strict";

// ajax get
function ajaxGet(urlString, callback) {
    let r = new XMLHttpRequest();
    r.open("GET", urlString, true);
    r.setRequestHeader("Content-Type", "text/plain;charset=UTF-8");
    r.send(null);
    r.onload = function() {
        callback(r.response);
    };
};

    // ввод ключа и отправка запроса на сервер
function getRecord() {
    // input fields
    const mail = document.getElementById("field-mail").value;
    
    const mail_a = encodeURIComponent(mail);
    const url = `/record?k=${mail_a}`;

    // label
    const label = document.getElementById("result-label");

    // отправка запроса на сервер
    ajaxGet(url, function(answerString) {
        const answerObject = JSON.parse(answerString);
        const result = answerObject.v;
        label.innerHTML = `Ответ: ${result}`;
    });
}