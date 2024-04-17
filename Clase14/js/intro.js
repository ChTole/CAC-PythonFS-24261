// Tipos de datos

// Primitivos
// Boolean, Number, BigInt, String, Symbol y undefined

// Complejos
// Array - arreglo (vector) --> Python: Listas
// Object - objeto (atributos y métodos) --> Python: Diccionarios
// null

// EJECUTAR EN LA CONSOLA
typeof 5 // 'number'
typeof 3.14 // 'number'
typeof 5n // 'bigint'
typeof true // 'boolean'
typeof True // 'undefined' --> 

// Debilmente tipado
typeof ("123" + 1) // 'string'

// Ver DOM
// https://developer.mozilla.org/es/docs/Web/API/Document_Object_Model/Introduction

// no es necesario colocar 'window' porque está implícito
window.console.log('Comenzamos la clase N° 14!!!');

// acceso a la etiqueta h1 y la muestro en la consola
console.log(document.querySelector("h1"));

// VARIABLES

// Declarar y luego asignar
// var: manera discontinua // NO RECOMENDABLE USAR
var miVariable; // declaración
console.log(miVariable); // undefined

miVariable = 5; // asignación
console.log(miVariable); // 5
console.log(typeof miVariable); // number

// FORZAR EL ERROR
var miVariable = 10; // declarar y asignar // no es correcto volver a declarar
console.log(miVariable); // 5
console.log(typeof miVariable); // number

// *****************************************
let otraVariable = 15;
// let otraVariable = new Number() // instancia de objeto: poco habitual
console.log(otraVariable, typeof otraVariable);

// let otraVariable = 20; // Uncaught SyntaxError: Identifier 'otraVariable' has already been declared
otraVariable = "Cadena de texto"; // tipado dinámico
console.log(otraVariable, typeof otraVariable);
otraVariable = true;
console.log(otraVariable, typeof otraVariable);

// Si necesito una constante
const miConstante = "Nadie me modifica";

console.log(miConstante, typeof miConstante);

miConstante = false; // Uncaught TypeError: Assignment to constant variable.
console.log(miConstante, typeof miConstante);
