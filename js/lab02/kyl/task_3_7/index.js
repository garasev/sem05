"use strict";

const fs = require("fs");
 
const node7 = {name: "7", child1: null, child2: null};
const node4 = {name: "4", child1: null, child2: null};
const node5 = {name: "5", child1: node7, child2: null};
const node6 = {name: "6", child1: null, child2: null};
const node2 = {name: "2", child1: node4, child2: node5};
const node3 = {name: "3", child1: node6, child2: null};
const node1 = {name: "1", child1: node2, child2: node3};
console.log(JSON.stringify(node1));
 
fs.writeFileSync("task7.txt", JSON.stringify(node1));
 
 
let longestbranch = "";
function search(node, branch) {
    branch += node.name;
    if (branch.length > longestbranch.length)
        longestbranch = branch;
    if (node.child1 !== null)
        search(node.child1, branch)
    if (node.child2 !== null)
        search(node.child2, branch)
}
 
const obj = JSON.parse(fs.readFileSync("task7.txt", "utf8"));
 
search(obj, "");
console.log(longestbranch);