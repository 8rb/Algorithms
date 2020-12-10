//unknown =! any

let userInput: unknown;
let userName: string;

userInput = 5;
userInput = 'Hello';

//you can't assign a type to unknown unless you are sure that are the same type
//Not this:
//userName = userInput;
//This:
if(typeof userInput === 'string') {
    userName = userInput;
}

//Never type, used when you return blank instead of undefined eg: errors
function generateError(message: string, code: number):never {
    throw {message: message, errorCode: code};
}

const res = generateError('An error ocurred', 500);
console.log(res);
