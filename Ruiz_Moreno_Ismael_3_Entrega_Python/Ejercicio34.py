opcion = 0

while opcion != 3:
    print("1. Mostrar mensaje")
    print("2. Mostrar fecha ficticia")
    print("3. Salir")

    opcion = int(input("Elige una opción: "))

    if opcion == 1:
        print("Hola, este es un mensaje")
    elif opcion == 2:
        print("Fecha: 01/01/2026")
    elif opcion == 3:
        print("Saliendo...")
    else:
        print("Opción incorrecta")
