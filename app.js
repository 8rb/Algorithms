"use strict";
exports.__esModule = true;
console.log("Hello Typescript");
function welcomePerson(person) {
    console.log("Hey " + person.firstname + " " + person.lastname);
    return "GAAAAA";
}
var roro = {
    firstname: "Rodrigo",
    lastname: "Ramirez"
};
welcomePerson(roro);
