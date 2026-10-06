stock = int(input("Introduce el stock disponible: "))
cantidad = int(input("Introduce la cantidad que quiere comprar: "))

if cantidad <= stock:
    print("Venta posible")
else:
    print("Stock insuficiente")
