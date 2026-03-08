
function mostrarMenu() {
    console.log("");
    console.log("---------------------------------------------------- Bienvenid@ al convertor de unidades ----------------------------------------------------");
    console.log("");
    console.log("para CELSIUS -> FAHRENHEIT coloque 1");
    console.log("para METROS -> KILOMETROS coloque 2");
    console.log("");
}


function pedir_numero(mensaje) {
    while (true) {
        let entrada = prompt(mensaje); 
        let numero = parsefloat(entrada);

        if (!isNaN(numero)) {
            return numero; 
        } else {
            console.log("Error: debe ingresar un número válido. Intente de nuevo.");
        }
    }
}


mostrarMenu();
let opcion = pedirNumero("Seleccione una opcion (1 o 2):");