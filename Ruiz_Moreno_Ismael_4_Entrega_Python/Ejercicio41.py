def buscar_producto(productos, nombre):
    encontrado = False

    for producto in productos:
        if producto == nombre:
            encontrado = True

    return encontrado

productos = ["Teclado", "Monitor", "Ratón", "Webcam"]

print(buscar_producto(productos, "Monitor"))
print(buscar_producto(productos, "Impresora"))
