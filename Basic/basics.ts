function add(n1: number, n2: number, show: boolean, result: string){

    const res = n1 + n2
    if(show){
        console.log(result + res);
    }
    else{
        return n1 + n2;
    }
}

let number0: number; //only before assignment
number0 = 69;
const number1 = 5;
const number2 = 2.8;
const printResult = true;
const result = 'Result is: ';

add(number1, number2, printResult, result);