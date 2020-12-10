//export default 

//explicit type for function void, number, string, etc...
function printRes(num: number):void {
    console.log('Result: ', num);
}
function add2(n1: number, n2: number): number {
    return n1 + n2;
}

//function as parameter
function AddAndHandle(n1: number, n2: number, cb: (num: number) => void) {
    const result = n1 + n2;
    cb(result);
}

//asigning a function type to a variable type
let answer: (a: number, b: number) => number;


//asigning a function to a variable
answer = add2;

//What you can't do:
//answer = 5;
//answer = printRes;

console.log(answer(5,5));

//printRes(add(5, 5));

//Calling the function that receives another function as a parameter
AddAndHandle(10,20, (result) => {
    console.log(result);
    return result;
});