// NOMBRES DE VARIABLES (ver palabras reservadas)
// - Pueden comenzar con una letra, un guión bajo ( _ ) o un signo de dólar ( $ ). (sintaxis y convención)
// - Los siguientes caracteres también pueden ser dígitos ( 0 - 9 ), nunca al principio (sintaxis). 
// - JavaScript distingue entre mayúsculas y minúsculas (es case-sensitive).
// - Cuando contienen más de una palabra se utiliza la notación camelCase (convención).
// - Deben ser referenciales de su contenido (convención).
let _miVariable; // _MIvAriable
let otraVariable;
let $variable;
let varNro4;
// let x = "datos_del_form";
let datosForm;

// OPERADORES
// Aritméticos: + , - , * , / , ** , %
let suma = 5.5 + 4; // expresión aritmética
console.log(suma);
let potenciaDeTres = 2 ** 3;
console.log(potenciaDeTres);
let nroPar = 9 % 2; // 1  <-- resto o módulo
console.log(nroPar);
let variasOperaciones = 3 ** 3 * 2 + 5 / 2 - 3 * 4
//                        27    * 2 + 2.5 - 12
//                           54 + 2.5 - 12
//                              44.5
console.log(variasOperaciones);


// De comparación: < , > , <= , >= , == , != (devuelven booleanos)
let mayorQue = 5 > 2;
console.log(mayorQue); // true
let parImpar = 9 % 2 == 0; // primero se resuelve la expresión aritmética, luego la comparación
console.log(parImpar);
let igualdad = "5" == 5; // debilmente tipado => compara literales
console.log(igualdad);
// Identidad === , !==
igualdad = "5" === 5; // reasignar el valor
console.log(igualdad);

console.log('*******************************');

// Lógicos: && (conjunción ó «y»), || (disyunción u «ó») y ! (negación -unario-)
// DEVUELVEN BOOLEANOS!!!
// 1ra proposición: si el día está lindo,      true   true
// 2da proposición: «Y» si tenemos tiempo,     true   false
// Resultado:       salimos a caminar.         true   false
// Conjunción 
let caminata = true && true;
console.log(caminata);  // true
caminata = true && false;
console.log(caminata);  // false
caminata = false && true;
console.log(caminata);  // false
caminata = false && false;
console.log(caminata);  // false

let operacionLogica = 5 >= 2 * 2 && "hola" != "HOLA"; // 1ro: aritmético, 2do: comparación, 3ro: lógico
//                    5 >= 4 && true
//                    true  && true
console.log(operacionLogica);

"A" == "a" // alt 65  A  // alt 97 a

// Disyunción: OR  ||  (alt 124) 
// 1ra:             Si vos estás en el shopping,                true
// 2da:             «O» yo estoy en el shopping,                false
// Resultado:       alguien le compra el regalo a mamá.         true

console.log(true || false); // true
console.log(false || true); // true
console.log(false || false); // false
console.log(true || true); // true

// Negación NOT  ! (operador unario)
console.log(!true); // false
console.log(!"hola" != "HOLA");
//          !    true      => 
let miExpresion = 3 ** 2 >= 54 % 4 || true && !(5 > 2);
//                                              true;
//                  9    >=    2   || true && false ;
//                       true || true && false
// Precedencia de operadores lógicos: negación -> conjunción -> disyunción
//                           true || false  = true
console.log(miExpresion);

// CUADROS DE DIÁLOGO (alert, prompt, confirm)
// No son de uso habitual, pero en éste punto nos sirven para interactuar con nuestra página, sitio o aplicación.
// Estos mensajes automatizados tienen dos inconvenientes:
// No hay una forma estándar de cambiar su aspecto con CSS.
// Dependen de la configuración regional del navegador, lo que significa que puedes tener una página en un idioma pero un mensaje de error en otro idioma.

// alert('Mensaje emergente!');
let dato = prompt('Ingrese un dato:'); // prompt siempre devuelve string
console.log(dato, typeof dato);
let confirmacion = confirm('Confirma operación:');
console.log(confirmacion); // confirm devuelve un booleano

// CONTROL DE FLUJO
// Estructuras condicionales (if - if...else - if...else if...else - switch...case)
// Estructuras repetitivas indeterminadas (while - do...while)
// Estructuras repetitivas determinadas (for (desde,hasta,paso) - for...of - for...in)