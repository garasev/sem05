"use strict";

function check_surname(surname, children) {
    for (let i = 0; i < children.length; i++) {
        if (children[i].surname === surname) {
            return false;
        }
    }
    return true;
}

function create_child(surname, age, children) {
    if (check_surname(surname, children)) {
        children.push({surname: surname, age: age});
    }
    else {
        console.log("ERROR. The child was not created because the surname (" + surname + ") is not unique")
    }
}

function print_one(child) {
    console.log(child);
}

function print_all(children) {
    for (let i = 0; i < children.length; i++) {
        print_one(children[i]);
    }
}

function update_surname(new_surname, child) {
    child.surname = new_surname;
}

function update_age(new_age, child) {
    child.age = new_age;
}

function update_child(new_surname, new_age, child) {
    update_surname(new_surname, child);
    update_age(new_age, child);
}

function delete_child(surname, children) {
    for (let i = 0; i < children.length; i++) {
        if (children[i].surname === surname) {
            children.splice(i,1);
            return;
        }
    }
}

// *****************************************************

function average_age(children) {
    if (children.length === 0) {
        return 0
    }

    let ave = 0;
    for (let i = 0; i < children.length; i++) {
        ave += children[i].age;
    }
    return ave / children.length
}

function max_age_child(children) {
    let elder = children[0];
    for (let i = 1; i < children.length; i++) {
        if (children[i].age > elder.age)
            elder = children[i];
    }
    return elder
}

function find_children_by_age(children, start, stop) {
    let found = [];
    for (let i = 0; i < children.length; i++) {
        if (children[i].age >= start && children[i].age <= stop) {
            found.push({surname:children[i].surname, age: children[i].age});
        }
    }
    return found;
}

function find_children_by_first_symbol(children, s) {
    let found = [];
    for (let i = 0; i < children.length; i++) {
        if (children[i].surname[0] === s)
            found.push({surname:children[i].surname, age: children[i].age});
    }
    return found;
}

function find_children_by_min_len(children, min_len) {
    let found = [];
    for (let i = 0; i < children.length; i++) {
        if (children[i].surname.length > min_len)
            found.push({surname:children[i].surname, age: children[i].age});
    }
    return found;
}

function find_children_by_vowel(children) {
    let vowel = ['A', 'E', 'U', 'Y', 'I', 'O'];
    let found = [];
    for (let i = 0; i < children.length; i++) {
        if (vowel.indexOf(children[i].surname[0], 0) != -1)
            found.push({surname:children[i].surname, age: children[i].age});
    }
    return found;
}

let children = [];

console.log("Creating");
create_child("Austin", 3, children);
create_child("Bush", 4, children);
create_child("Conors", 5, children);
create_child("Dyson", 8, children);
create_child("Donaldson", 6, children);
create_child("Ford", 7, children);
create_child("Goodman", 6, children);
create_child("Harrison", 3, children);
create_child("Mackenzie", 4, children);
console.log("\nAll children:");
print_all(children);

console.log("\nChild update");
update_child("Adamson", 2, children[0]);
print_one(children[0]);

console.log("\nDeleting Mackenzie");
delete_child("Mackenzie", children);
console.log("\nAll children:");
print_all(children);

console.log("\nAverange age:")
console.log(average_age(children));

console.log("\nOlder child:");
console.log(max_age_child(children));

console.log("\nNeed children 1-4:");
console.log(find_children_by_age(children, 1, 4));
console.log("\nNeed children 5-10:");
console.log(find_children_by_age(children, 5, 10));

console.log("\nChildren Begin Surname D:");
console.log(find_children_by_first_symbol(children, 'D'));

console.log("\nChildren with longer surname 5 count of symbols:");
console.log(find_children_by_min_len(children, 5));

console.log("\nChildren Begin Vowel surname:");
console.log(find_children_by_vowel(children));