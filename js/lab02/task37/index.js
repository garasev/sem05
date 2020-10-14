"use strict";

const fs = require("fs");
 
const node9 = {name: "9", child1: null, child2: null};
const node8 = {name: "8", child1: node9, child2: null};
const node7 = {name: "7", child1: null, child2: null};
const node6 = {name: "6", child1: null, child2: null};
const node5 = {name: "5", child1: null, child2: null};
const node4 = {name: "4", child1: node7, child2: node8};
const node3 = {name: "3", child1: node5, child2: node6};
const node2 = {name: "2", child1: node3, child2: node4};
const node1 = {name: "1", child1: node2, child2: null};
console.log(JSON.stringify(node1));
 
fs.writeFileSync("tree.txt", JSON.stringify(node1));
 
 
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
 
const obj = JSON.parse(fs.readFileSync("tree.txt", "utf8"));
 
search(obj, "");
console.log(longestbranch);