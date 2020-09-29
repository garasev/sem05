"use strict";

// проверка уникальности имени точки
function check_name(name, points) {
    for (let i = 0; i < points.length; i++) {
        if (points[i].name === name) {
            return false;
        }
    }
    return true;
}

// создание точки
function create_point(name, pointX, pointY, points) {
    if (check_name(name, points)) {
        points.push( {
            name: name, 
            x: pointX,
            y: pointY
        });
    }
    else {
        console.log("ERROR. The Point was not created because the name (" + name + ") is not unique")
    }
}

// чтение информации точки
function print_one(point) {
    console.log(point);
}

// чтение информации точек
function print_all(points) {
    for (let i = 0; i < points.length; i++) {
        print_one(points[i]);
    }
}

// обновить имя точки
function update_name(new_name, point) {
    point.name = new_name;
}

// обновить абсциссу точки
function update_x(new_x, point) {
    point.x = new_x;
}

// обновить ординату точки
function update_y(new_y, point) {
    point.y = new_y;
}

// обновить все данные о точки
function update_all(new_name, new_x, new_y, point) {
    update_name(new_name, point);
    update_x(new_x, point);
    update_y(new_y, point);
}

// удалить точку
function delete_point(name, points) {
    for (let i = 0; i < points.length; i++) {
        if (points[i].name === name) {
            points.splice(i,1);
            return;
        }
    }
}

// расстояние между двумя точками
function distance(point_a, point_b) {
    let dx = point_b.x - point_a.x;
    let dy = point_b.y - point_a.y;
    return Math.sqrt(dx * dx + dy * dy);
}

// получение двух точек, между которыми наибольшее расстояние
function find_max_distance(points) {
    let mdist = 0;
    let find_point = [];
    let dist;
    for (let i = 0; i < points.length - 1; i++) {
        for (let j = i + 1; j < points.length; j++) {
            dist = distance(points[i], points[j]);
            if (dist > mdist) {
                find_point = [];
                find_point.push([points[i],points[j]]);
                mdist = dist;
            } else if (dist == mdist) {
                find_point.push([points[i],points[j]]);
            }
        }
    }
    return find_point;
}

// получение точек, находящихся от заданной точки на расстоянии, не превышающем заданную константу
function find_points_less_dist(set_point, dist, points) {
    let find_point = [];
    for (let i = 0; i < points.length; i++) {
        if (points[i] != set_point) {           
            if (distance(points[i], set_point) <= dist) {
                find_point.push(points[i]);
            }
        }
    }
    return find_point;
}

// получение точек, находящихся выше / ниже оси абсцисс
function find_point_ox(dir, points) {
    let find_point = [];
    if (dir === "above" || dir === "below") {
        for (let i = 0; i < points.length; i++) {
            if (dir === "above") {
                if (points[i].y > 0) {
                    find_point.push(points[i]);
                }
            } else {
                if (points[i].y < 0) {
                    find_point.push(points[i]);
                }
            } 
        }
    } else {
        console.log("incorrect direction");
    }
    return find_point;
}

// получение точек, находящихся левее / правее оси ординат
function find_point_oy(dir, points) {
    let find_point = [];
    if (dir === "left" || dir === "right") {
        for (let i = 0; i < points.length; i++) {
            if (dir === "left") {
                if (points[i].x < 0) {
                    find_point.push(points[i]);
                }
            } else {
                if (points[i].x > 0) {
                    find_point.push(points[i]);
                }
            } 
        }
    } else {
        console.log("incorrect direction");
    }
    return find_point;
}

// получение точек, входящих внутри заданной прямоугольной зоны
// прямоугольник задается точкой нижнего левого угла, шириной и высотой
function rect_check(x, y, width, height, points) {
    let find_point = [];
    for (let i = 0; i < points.length; i++) {
        if (points[i].x > x && points[i].x < (x + width) && points[i].y > y && points[i].y < (y + height)) {
            find_point.push(points[i]);
        } 
    }
    return find_point;
}

let points = [];

console.log("Creating");
create_point("1", -1, 1, points);
create_point("2", 1, 1, points);
create_point("3", 1, -1, points);
create_point("2", -1, -1, points);
create_point("4", -10, -10, points);
create_point("5", 0, 0, points);
create_point("6", 0, 0, points)
print_all(points);

console.log("\nDeleting five point");
delete_point("5", points);
print_all(points);

console.log("\nUpdate our point");
print_one(points[3]);
update_all("4", -1, -1, points[3]);
print_one(points[3]);

console.log("\nFind point with max distance");
console.log(find_max_distance(points));

console.log("\nFind point with set distance");
console.log("set distanse 5:");
console.log(find_points_less_dist(points[3], 5, points));
console.log("set distanse 2:");
console.log(find_points_less_dist(points[3], 2, points));


console.log("\nFind point above from axis OX");
console.log(find_point_ox("above", points));
console.log("\nFind point below from axis OX");
console.log(find_point_ox("below", points));
console.log("\nFind point left from axis OY");
console.log(find_point_oy("left", points));
console.log("\nFind point right from axis OY");
console.log(find_point_oy("right", points));

console.log("\nCheck if incorrect direction")
console.log(find_point_ox("1", points));
console.log(find_point_oy("2", points));


console.log("\nCheck in Rectangle");
console.log(rect_check(-2, -2, 5, 5, points));
console.log(rect_check(-1, -1, 2, 2, points));
console.log(rect_check(-0.5, -0.5, 0.1, 0.1, points));
