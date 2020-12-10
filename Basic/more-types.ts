//Specialised object type
// const person: {
//     name: string;
//     age: number;
// } = {
//     name: 'Rodrigo',
//     age: 20,
// }

enum Role {ADMIN, READ_ONLY, AUTHOR};

const person: {
    name: string;
    age: number;
    hobbies: string[];
    role: number | string;
} = {
    name: 'Rodrigo',
    age: 20,
    hobbies: ['Sports', 'Cooking'],
    role: Role.ADMIN
}

//Tuple:
//role: [number, string];
//person.role[1] = 5;

let favoriteActivities: string[];
favoriteActivities = ['10'];


console.log(person.name)

for (const hobby of person.hobbies) {
    console.log(hobby.toUpperCase())
}

if (person.role === Role.ADMIN) {
    console.log('is admin')
}