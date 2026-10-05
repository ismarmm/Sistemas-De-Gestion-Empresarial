productos = [
    "Teclado",
    "Ratón",
    "Monitor",
    "Webcam",
    "Impresora"
]

producto = input("Introduce un producto: ")

if producto in productos:
    print("Producto encontrado")
else:
    print("Producto no encontrado")