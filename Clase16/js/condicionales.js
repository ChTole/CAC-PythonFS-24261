// Repaso operadores
// Operaciones: 1° aritméticos, 2° comparaciones (e identidad), 3° lógicos
let expresion = 6 * 2 > 2 ** 4 && "hola" != "chau" || (4 / 2) < 4 ** (1/2)
//              12    >   16   &&       true       ||    2    <    2
//                  false      &&       true       ||        false
//                          false                  ||        false      = false

// CONTROL DE FLUJO

// Estructuras condicionales (if - if...else - if...else if...else - switch...case)
console.log('Comienzo');
let edad = 1400;
console.log('Dato de edad obtenido:', edad)

// Mayoría de edad
// 18 - 19 ...
// edad > 17
// DATO SIN VALIDACIÓN
if (edad >= 18) { // se ejecuta si la condición devuelve true
    console.log("Sos mayor de edad");
} else { // se ejecuta cuando la condición devuelve false
    console.log("Sos menor de edad");
}

// if (edad < 18) { // redundante e ineficiente
//     console.log("Sos menor de edad");
// }

// Situación ante votación (en Argentina)
// menor a 16: aún no puede votar
// 16 ó 17: puedo votar, pero no es obligatorio
// 18 hasta 70: es obligatorio votar
// mayor a 70: puedo votar, pero no es obligatorio

// console.log(isNaN(edad));

// PRIMERO: VALIDACIÓN DEL DATO
if (edad >= 0 && edad <= 120) {
    // LUEGO: RESUELVO MI PROBLEMA
    if (edad == 16 || edad == 17 || edad > 70) {
        console.log('Podés votar, no es obligatorio.');
    } else if (edad < 16) {
        console.log('Aún no podés votar.');
    } else {
        console.log('Es obligatorio tu voto.');
    }
} else {
    console.warn('Dato inválido!');
}

// Grupos sanguineos: 0 - A - B - AB  //  Factor: Rh+ ó Rh-
let grupoSanguineo = "A";
// switch - case
switch (grupoSanguineo) {
    // case "0+": puede evaluar más de una caso para un misma respuesta
    // case "0-":   
    case "0": 
        console.log("Dador universal.");
        break; // Necesito break para salir del bloque
    case "A":
        console.log('Grupo A');
        break;
    case 'B':
        console.log('Grupo B');
        break;
    case 'AB':
        console.log("Receptor universal.");
        break;
    default:
        console.warn('Grupo desconocido.')
}

console.log('Fin del algoritmo');
// Estructuras repetitivas indeterminadas (while - do...while)

// Estructuras repetitivas determinadas (for (desde,hasta,paso) - for...of - for...in)