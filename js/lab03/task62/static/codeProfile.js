"use strict";

    
function ajaxGet(urlString, callback) {
    let r = new XMLHttpRequest();
    r.open("GET", urlString, true);
    r.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    r.send(null);
    r.onload = function() {
        callback(r.response);
    }
}
    
function makeAction() {   
    const label = document.getElementById("result-label");
    const url = `/info`
    ajaxGet(url, function(answerString) {
        const obj = JSON.parse(answerString);
        label.innerHTML = `Логин: ${obj.login} Возраст: ${obj.age} Хобби: ${obj.hobby}`
    });
}