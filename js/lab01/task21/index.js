"use strict";

class Point {
    constructor(x,  y) {
        this.x = x;
        this.y = y;
    }

    console_log() {
        let start = " point coord: \n"
        let ox = "   x: " + this.x + "\n";
        let oy = "   y: " + this.y + "\n";
        let message = start + ox + oy;
        console.log(message);
    }
}

class Cut {
    constructor(x1, y1, x2, y2) {
        this.start = new Point(x1, y1);
        this.end = new Point(x2, y2);
    }

    console_log() {
        console.log("First point: ");
        this.start.console_log();
        console.log("Second point: ");
        this.end.console_log();
    }

    get_length() {
        let dx = this.end.x - this.start.x;
        let dy = this.end.y - this.start.y;
        return Math.sqrt(dx * dx + dy * dy);
    }
}

console.log("Start program.");

let point = new Point(3.5, 4);
point.console_log();

let cut = new Cut (0, 0, 6, 8); 
cut.console_log();

let len = cut.get_length();
console.log("Length cut is ", len);