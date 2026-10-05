clientes = [
    {
        "nombre": "Ana",
        "email": "ana@email.com",
        "ciudad": "Sevilla"
    },
    {
        "nombre": "Luis",
        "email": "luis@email.com",
        "ciudad": "Córdoba"
    },
    {
        "nombre": "Carlos",
        "email": "carlos@email.com",
        "ciudad": "Málaga"
    }
]

email = input("Introduce el email: ")

for cliente in clientes:
    if cliente["email"] == email:
        print("Cliente encontrado:")
        print("Nombre:", cliente["nombre"])
        print("Ciudad:", cliente["ciudad"])
        break
else:
    print("No existe ningún cliente con ese email.")