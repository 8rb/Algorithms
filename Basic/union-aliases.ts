//Just to avoid typing console.log .......
function pri(data: any) {
    console.log(data);
}

//alias
type Combinable = number | string;
type Conversion = 'as-number' | 'as-string';

//Union type
function combine(
    input1: Combinable,
    input2: Combinable, 
    conversionType: Conversion,
    ) {
    let result;
    if(typeof input1 === 'number' && typeof input2 === 'number' || conversionType === 'as-number') {
        result = +input1 + +input2;
    }
    else {
        result = input1.toString() + input2.toString(); //Explicitly convert to string
    }

    return result;
}

pri(combine(1, 6, 'as-number'));
pri(combine('1', 'A', 'as-number'));