// Introducción a funciones en JS
// Tiempos
// - 1° Declaración o definición
function saludar() {
    let usuario = "Christian";
    let frase = `Hola, soy ${usuario}`;
    console.log(frase);
}

// - 2° Invocación o llamada
saludar();

// Parámetros
function saludarPersona(nombre) {
    let frase = `Hola, soy ${nombre}`;
    console.log(frase);
}

saludarPersona('Ariel');
saludarPersona(); // undefined