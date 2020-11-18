console.log("Hello Typescript");

function welcomePerson(person: Person):string {
    console.log(`Hey ${person.firstname} ${person.lastname}`);
    return "GAAAAA";
}

const roro = {
    firstname: "Rodrigo",
    lastname: "Ramirez"
}

welcomePerson(roro);

interface Person {
    firstname: string,
    lastname: string
}
