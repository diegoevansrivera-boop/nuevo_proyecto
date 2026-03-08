bandera = True
while bandera:
    print("")
    print("---------------------------------------------------- Bienvenid@ al convertor de unidades ----------------------------------------------------")
    print("")
    print("para CELSIUS -> FAHRENHEIT coloque 1")
    print("para METROS -> KILOMETROS coloque 2")
    print("")

    while True:
        try:
            OPCION = int(input("Seleccione una opción: "))
            break
        except ValueError:
            print("Error: debe ingresar un número (1 o 2) Intente de nuevo.")

    if OPCION == 1:
        while True:
            try:
                Celsius = float(input("Ponga la temperatura en Celsius: "))
                resultado = (9/5 * Celsius) + 32
                print("")
                print(Celsius, "°C en Fahrenheit son:", resultado, "°F")
                break
            except ValueError:
                print("Error: solo se permiten números. Intente de nuevo")
    elif OPCION == 2:
        while True:
            try:
                metros = float(input("Ponga los metros a convertir: "))
                resultado = metros / 1000
                print("")
                print(metros, "mts en kilómetros son:", resultado, "km")
                break
            except ValueError:
                print("Error: solo se permiten números. Intente de nuevo")
    else:
        print("Formato incorrecto, solo se toman en cuenta las opciones 1 y 2")

    bandera = False

print("")
print("Fin del programa, ¡ten un feliz resto de día! :)")