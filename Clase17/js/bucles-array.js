// for...of - for...in

// Datos complejos: Array
// Propiedades:
// - Orden: son ordenados
// - Tipo de datos: cualquier tipo de dato (primitivo o complejo) => heterógeneos
// - Mutabilidad:
let lenguajes = ['Python', 'Pascal', 'Fortran', 'Java', 'Cobol', 'PHP'];
//                 0        1          2         3         4       5

lenguajes.push('SQL');
lenguajes[4] = 'Basic';
console.log(lenguajes[0]);
console.log(lenguajes);
console.log(lenguajes.length);
console.log(typeof lenguajes); // object
console.log(lenguajes instanceof Array); // true

// Ejemplo POO
// class Persona {}; // object --> super o prototipo

// class Usuarios extends Persona {}; // object // instancia: Persona (molde)
// class Admin extends Persona {}; // object // instancia: Persona (molde)

let listaArray = document.querySelector('#listaArray');

for (let i=0; i < lenguajes.length; i++) {
    // console.log(lenguajes[i]);
    let item = document.createElement('li');
    item.innerHTML = `${lenguajes[i]}`; // Python: f'{dato}'
    listaArray.appendChild(item);
}