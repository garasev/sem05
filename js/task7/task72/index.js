"use strict";

const execSync = require('child_process').execSync;

// функция для вызова программы и получения результата её работы
function useCmd(s) {
	const options = {encoding: 'utf8'};
	const cmd = s.toString();
	const answer = execSync(cmd, options);
	return answer.toString();
}

// получаем параметры скрипта
const type = "" + process.argv[2];
if (type === "number") {
    const number = "" + process.argv[3];
    // получаем факториал числа
    const factorialCommand = `node number.js ${number}`;
    console.log(factorialCommand);
    let factorial = useCmd(factorialCommand);
    factorial = parseInt(factorial);
    console.log(factorial);
} else if (type === "array") {
    let count = "" + process.argv[3];
    count = parseInt(count);
    let element;
    let array = [];
    for (let i = 4; i < count + 4 ; i++) {
        element = "" + process.argv[i];
        array.push(element);
    }
    // получаем факториал числа
    const factorialCommand = `node array.js ${array}`;
    console.log(factorialCommand);
    let factorial = useCmd(factorialCommand);
    console.log(factorial);
} else {
    console.log("incorrect key");
}