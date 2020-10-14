"use strict";

let exObj = {name: "obj0", child:null};
for (let i = 1;;i++) {
    try {
        const obj = {name: "obj" + i, child: exObj};
        JSON.stringify(obj);
        exObj = obj;
    } catch (err) {
        console.log(err);
        console.log(i);
        break;
    }
}