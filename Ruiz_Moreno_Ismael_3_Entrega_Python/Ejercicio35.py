venta = float(input("Introduce una venta (0 para terminar): "))

contador = 0
total = 0

while venta != 0:
    contador = contador + 1
    total = total + venta
    venta = float(input("Introduce una venta (0 para terminar): "))

print("Número de ventas:", contador)
print("Total vendido:", total, "€")
