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
        "ciudad": "Sevilla"
    },
    {
        "nombre": "Laura",
        "email": "laura@email.com",
        "ciudad": "Sevilla"
    }
]

ciudad = input("Introduce una ciudad: ")

contador = 0

for cliente in clientes:
    if cliente["ciudad"] == ciudad:
        contador += 1

print("Número de clientes de", ciudad + ":", contador)