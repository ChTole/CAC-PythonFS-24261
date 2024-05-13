// Validar formulario
console.log('Comienzo');

function validarDatos(){
    let nombre = document.querySelector('#nombre').value;
    let edad = document.querySelector('#edad').value;
    
    // Expresión regular
    let soloPalabras = /^[a-z\s]+$/i;
    // console.log(soloPalabras.test('Christian'));
    // console.log(soloPalabras.test('chrisTian'));
    // console.log(soloPalabras.test('chrisTian Ariel'));
    // console.log(soloPalabras.test('chrisTian 1324'));

    let validos = true; // bandera o hipótesis
    let msgError = 'Datos inválidos: ';
    console.log(nombre);
    console.log(edad);
    // if (nombre === '') {
    if (!soloPalabras.test(nombre)) {
        validos = false;
        msgError += " nombre "
    }

    if (edad === '' || !Number.isInteger(Number(edad))) { 
        validos = false;
        msgError += " edad "
    }

    if (validos) {
        console.log('Datos ingresados correctamente.')
    } else {
        console.log(msgError);
    }
}


const formulario = document.querySelector('#formNombreEdad');
let mensaje = document.querySelector('#rtaForm');

formulario.addEventListener('submit', evento => {
    // mensaje.innerHTML = 'presionado';
    // console.log('presionado')
    validarDatos();
    evento.preventDefault();
})


console.log('Fin del algoritmo');