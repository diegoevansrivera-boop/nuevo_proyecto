// Convertor de Unidades en JavaScript

function mostrarMenu() {
    console.log("");
    console.log("---------------------------------------------------- Bienvenid@ al convertor de unidades ----------------------------------------------------");
    console.log("");
    console.log("para CELSIUS -> FAHRENHEIT coloque 1");
    console.log("para METROS -> KILOMETROS coloque 2");
    console.log("");
}

// Función para pedir un número válido
function pedirNumero(mensaje) {
    while (true) {
        let entrada = prompt(mensaje); // prompt devuelve string
        let numero = parseFloat(entrada); // convertir a número

        if (!isNaN(numero)) {
            return numero; // si es válido, lo devuelve
        } else {
            console.log("Error: debe ingresar un número válido. Intente de nuevo.");
        }
    }
}

// Programa principal
mostrarMenu();
let opcion = pedirNumero("Seleccione una opción (1 o 2):");

if (opcion === 1) {
    let celsius = pedirNumero("Ponga la temperatura en Celsius:");
    let resultado = (9/5 * celsius) + 32;
    console.log(`${celsius} °C en Fahrenheit son: ${resultado} °F`);
} else if (opcion === 2) {
    let metros = pedirNumero("Ponga los metros a convertir:");
    let resultado = metros / 1000;
    console.log(`${metros} mts en kilómetros son: ${resultado} km`);
} else {
    console.log("Formato incorrecto, solo se toman en cuenta las opciones 1 y 2");
}

console.log("");
console.log("Fin del programa, ¡ten un feliz resto de día! :)");