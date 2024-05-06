// Repaso array´s

// Propiedades:
// - Orden: tienen índice => son ordenados
// - Tipo de datos: cualquier tipo => heterógeneos
// - Mutabilidad: puedo modificar la cantidad y los elementos

let lista = []; //
console.log(lista);
console.log(lista.length);

lista.push('Soy una cadena'); // agrega al final
console.log(lista);

lista.unshift(true); // agrega al principio
console.log(lista);

lista.push(["a", 1, 3.14]); // agrego un array
console.log(lista);

lista.pop(); // "reviento" el último
console.log(lista);

lista[0] = "Es falso";
console.log(lista);

// Objects => pares clave: valor
let mascota = {
    nombre: 'Leia',
    felino: true
}

console.log(mascota);
console.log(typeof mascota);

// Propiedades
// Orden: no es ordenado
console.log(mascota.nombre);
console.log(mascota["nombre"]);

// Tipo de dato
// clave --> array no, object no // Number si, string también. => Primitivos si, colecciones no.
// let otraMascota = {
//     nombre: "Naranjo",
//     "duerme solo": false
// }
// console.log(otraMascota["duerme solo"]);

// valor --> cualquier tipo
let otraMascota = {
    nombre: "Naranjo",
    edad: "7 / 8 años",
    vidas: [1, 2, 3, 4, 5, 6, 7, 8],
    color: {
        1: "naranja",
        2: "blanco"
    }
}

// console.log(otraMascota);

// for...in
for (let clave in otraMascota) {
    console.log(`clave: ${clave} - valor: ${otraMascota[clave]}`);
}

// for...of
console.log(Object.keys(otraMascota)); // método estático

for (let clave of Object.keys(otraMascota)){
    console.log(clave); 
}

// mutabilidad

otraMascota.nombre = "Naranjo Godoy Toledo"; // reasignar un valor
console.log(otraMascota);

delete otraMascota.vidas; // borro el par clave:valor
console.log(otraMascota);

console.log(otraMascota.vidas); // undefined

otraMascota.edad = "7 años"; // las claves son únicas
otraMascota.sexo = "macho";
console.log(otraMascota);


