"use strict";

function ajaxPost(urlString, bodyString, callback) {
    let r = new XMLHttpRequest();
    r.open("POST", urlString, true);
    r.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    r.send(bodyString);
    r.onload = function() {
        callback(r.response);
    }
}

function makeAction() {
    // input fields
    const mail = document.getElementById("field-mail").value;
    const surname = document.getElementById("field-surname").value;
    const phone = document.getElementById("field-phone").value;

    // label
    const label = document.getElementById("result-label");

    ajaxPost("/save/info", JSON.stringify({
        mail, surname, phone
    }), function(answerString) {
        const answerObject = JSON.parse(answerString);
        const answer = answerObject.answer;
        alert(answer);
        const curFile = answerObject.curFile;
        label.innerHTML = `Текущий файл: ${curFile}`;
    });
}