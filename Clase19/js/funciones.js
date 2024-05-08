// Funciones
// 2 Tiempos: definición e invocación.

// Sin parámetros ni retorno
function saludar() {
    let nombre = 'Christian';
    let frase = `Hola, soy ${nombre}`;
    console.log(frase);
}
saludar();

// Con parámetros, sin retorno
function saludarPersona(nombre) {
    let frase = `Hola, soy ${nombre}`;
    console.log(frase);
}

saludarPersona('Ariel');
saludarPersona(); // undefined

// Con parámetros y retorno
function retornarSaludo(nombre, comision) {
    return `Hola, soy ${nombre}, de la comisión ${comision}`
}

let frase = retornarSaludo('Christian', 24261) + ' y estoy en Codo a Codo.';
console.log(frase);

// Funciones como expresiones
const llamar = function discarNumero(numero) { // función como expresión, el nombre no es accesible
    console.log(`Llamando a ${numero}`);
}

llamar(1122223333);
// discarNumero(5558888); // Lanza excepción, no definida

// Funciones anónimas
const llamarCelular = function(numero) { // función anónima
    console.log(`Llamando a ${numero}`);
}

llamarCelular(1188887777);

// IIFE (Expresión de función inmediamente invocada)
(function(mensaje){
    // mensaje y frase son de ámbito local, no existen fuera de la función
    // la variable frase ya existe en el ámbito global
    let frase = `Mensaje: ${mensaje}`; // sombreado, NO ES UNA BUENA PRÁCTICA
    console.log(frase);
})('Clase de funciones');

// console.log(mensaje); // no estás definido de manera global

// Callback
let recorrer = function(elemento, indice) {
    console.log(`indice: ${indice} - elemento: ${elemento}`);
}

let lenguajes = ['Python', 'PHP', 'JavaScript'];

lenguajes.forEach(recorrer); // recorrer es el callback => función como argumento

// Función flecha
lenguajes.forEach((elemento, indice) => { // función flecha
    console.log(`indice: ${indice} - elemento: ${elemento}`);
});

let cuadrado = numero => numero * numero; // no es necesario el return

console.log(cuadrado(2));