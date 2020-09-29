"use strict";

function check_card(card, student) {
    for (let i = 0; i < student.length; i++) {
        if (student[i].card === card) {
            console.log(student[i]);
            return false;
        }
    }
    return true;
}

// создание студента
function create_student(group, card, mark, student) {
    if (check_card(card, student)) {
        student.push( {
            group: group, 
            card: card,
            mark: mark 
        });
    }
    else {
        console.log("ERROR. The student was not created because the card (" + card + ") is not unique")
    }
}

// прочтение информации о студенте
function print_one(student) {
    console.log(student);
}

// прочтение информации о студентах
function print_all(student) {
    for (let i = 0; i < student.length; i++) {
        print_one(student[i]);
    }
}

// обновить группу студента
function update_group(newGroup, student) {
    student.group = newGroup;
}

// обновить студенческий билет студента
function update_card(card, student) {
    student.card = card;
}

// обновить оценки студента
function update_mark(newMark, student) {
    student.mark = newMark;
}

// обновить данные студента
function update_all(new_group, new_card, new_mark, student) {
    update_group(new_group, student);
    update_card(new_card, student);
    update_mark(new_mark, student);
}

// удалить студента
function delete_student(card, student) {
    for (let i = 0; i < student.length; i++) {
        if (student[i].card === card) {
            student.splice(i,1);
            return;
        }
    }
}

// нвхождение средней оценки студента
function averange_mark(student) {
    if (student.mark.length == 0)
        return 0;

    let mark = 0;

    for (let i = 0; i < student.mark.length; i++) {
        mark += student.mark[i];
    }
    return mark / student.mark.length
}

// получение информации о студентах в заданной группе
function get_student(group, student) {
    let groups = [];
    for (let i = 0; i < student.length; i++) {
        if (student[i].group === group) {
            groups.push(student[i]);
        }
    }
    return groups;
}

// максимальное кол-во оценок у студентов
function find_max_cnt_mark(student) {
    let mcount = 0;
    for (let i = 0; i < student.length; i++) {
        if (student[i].mark.length > mcount) {
            mcount = student[i].mark.length;
        }
    }
    return mcount;
}

// получение студента, у которого наибольшее количество оценок в заданной группе
function find_student_with_max_count(student) {
    let students = [];
    let mcount = find_max_cnt_mark(student);
    for (let i = 0; i < student.length; i++) {
        if (student[i].mark.length == mcount) {
            students.push(student[i]);
        }
    }
    return students;
}

// получение студента, у которого нет оценок
function find_student_without_mark(student) {
    let students = [];
    for (let i = 0; i < student.length; i++) {
        if (student[i].mark.length == 0) {
            students.push(student[i]);
        }
    }
    return students;
}

let student = [];

console.log("Creating");
create_student("IU7-52", 10, [5, 4, 3], student);
create_student("IU7-51", 11, [5, 3], student);
create_student("IU7-52", 12, [5], student);
create_student("IU7-53", 13, [5, 2, 5], student);
create_student("IU7-53", 14, [4, 3, 3], student);
create_student("IU7-52", 15, [4, 3], student);
create_student("IU7-51", 16, [2, 1], student);
create_student("IU7-53", 17, [2, 2], student);
create_student("IU7-54", 18, [], student);
print_all(student);

console.log("\nDelete Student 12");
delete_student(12, student);
print_all(student);

console.log("\nUpdate Student[5]");
console.log("Before");
print_all(student[5]);
update_all("IU7-54", 118, [3, 4, 5], student[5]);
console.log("After");
print_one(student[5]);

console.log("\nAverange mark student[0]");
console.log(averange_mark(student[0]));
console.log("\nAverange mark student[6]");
console.log(averange_mark(student[6]));

console.log("\nStudents from group IU7-52");
console.log(get_student("IU7-52", student));

console.log("\nStudent with the most marks");
console.log(find_student_with_max_count(student));

console.log("\nStudent with no marks");
console.log(find_student_without_mark(student));