"use strict";

let count = 0;
let needCount = 2;

function printNumber(delay, stage){
    let num = 0;
    let interval = setInterval(() => {
        if (num >= 0) {
            num++;
            if (stage === 0) {
                console.log(num);
            } else {
                console.log(num + 10);
            }
        }
        
        if (num === 10) {
            clearInterval(interval);
            num = 0;
            if (stage === 0) {
                printNumber(1000, 1);
            } else {
                count++;
                if (count != needCount) {
                    printNumber(2000, 0);
                }
            }
        };
    }, delay);
}

printNumber(2000, 0);