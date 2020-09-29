"use strict";

class Triangle {
    constructor(a,  b, c) {
        this.a = a;
        this.b = b;
        this.c = c;
    }

    console_log() {
        let start = " triangle len: \n"
        let a = "   a: " + this.a + "\n";
        let b = "   b: " + this.b + "\n";
        let c = "   b: " + this.c + "\n";
        let message = start + a + b + c;
        console.log(message);
    }

    triangle_check() {
        if ((this.a + this.b > this.c) && (this.a + this.c > this.b) && (this.c + this.b > this.a)) {
            return true;
        }
        return false;
    }

    hypotenuse(leg1, leg2, hypotense) {
        if ((leg1 * leg1 + leg2 * leg2) == hypotense * hypotense) {
            return true;
        }
        return false;
    }

    rectangular() {
        if (this.triangle_check()) {
            let tmp = Math.max(this.a, this.b, this.c);
            if (tmp == this.a) {
                return this.hypotenuse(this.b, this.c, tmp);
            } else if (tmp == this.b) {
                return this.hypotenuse(this.a, this.c, tmp);
            } else {
                return this.hypotenuse(this.a, this.b, tmp);
            }
        }
        return NaN;
    }

    perimetr() {
        if (this.triangle_check()) {
            return this.a + this.b + this.c;
        }
        return NaN;
    }

    square() {
        if (this.triangle_check()) {
            let p = this.perimetr() / 2;
            return Math.sqrt(p * (p - this.a) * (p - this.b) * (p - this.c));
        }
        return NaN;
    }
}

let triangle = new Triangle(10, 9, 11);
console.log("Data: 10, 9, 11");
console.log("Is it triangle?");
console.log(triangle.triangle_check());
console.log("Perimetr = ", triangle.perimetr());
console.log("Square = ", triangle.square());
console.log("Is it rectangular triangle?");
console.log(triangle.rectangular());

let triangle1 = new Triangle(15, 15, 15);
console.log("Data: 15, 15, 15");
console.log("Is it triangle?");
console.log(triangle1.triangle_check());
console.log("Perimetr = ", triangle1.perimetr());
console.log("Square = ", triangle1.square());
console.log("Is it rectangular triangle?");
console.log(triangle1.rectangular());

let triangle2 = new Triangle(3, 4, 5);
console.log("Data: 3, 4, 5");
console.log("Is it triangle?");
console.log(triangle2.triangle_check());
console.log("Perimetr = ", triangle2.perimetr());
console.log("Square = ", triangle2.square());
console.log("Is it rectangular triangle?");
console.log(triangle2.rectangular());