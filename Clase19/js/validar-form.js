// Validar formulario
console.log('Comienzo');

const formulario = document.querySelector('#formNombreEdad');
let mensaje = document.querySelector('#rtaForm');

formulario.addEventListener('submit', evento => {
    mensaje.innerHTML = 'presionado';
    console.log('presionado')
    evento.preventDefault();
})


console.log('Fin del algoritmo');