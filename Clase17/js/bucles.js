// Estructuras repetitivas indeterminadas (while - do...while)
// Porque la repetición está sujeta a una condición.
let limite = 0; // probar con otro valor para ver como se comportar los bucles
let contador = 0;
let lista = document.querySelector('#listaWhile'); // querySelector: mismas llamadas que en CSS
console.log(lista);
let encabezado = document.querySelector('h1');
console.log(encabezado);

while (contador < limite) {
    let item = document.createElement('li');
    item.innerHTML = `Dato dinámico N° ${contador}`; // Modifico el atributo de la etiqueta
    lista.appendChild(item); // método para agregar elementos "hijos"
    contador++ // contador = contador + 1
}

let lista2 = document.querySelector('#listaDoWhile');

do {
    // Se ejecuta por lo menos una vez
    let item = document.createElement('li');
    item.innerHTML = `Dato dinámico N° ${contador}`;
    lista2.appendChild(item);
    contador++
} while (contador < limite);

// Estructuras repetitivas determinadas (for (desde;hasta;paso) - for...of - for...in)
// Recorriendo/iterando algo.

let lista3 = document.querySelector('#listaFor');

for (let vuelta = 1; vuelta <= 5; vuelta++) {
    // vuelta= 1 -> 2 -> 3 ... 5
    let item = document.createElement('li');
    item.innerHTML = `Dato dinámico N° ${vuelta}`;
    lista3.appendChild(item);
}