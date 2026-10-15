def calcular_total(ventas):
    total = 0

    for venta in ventas:
        total = total + venta

    return total

ventas = [120.50, 80, 35.90, 220, 15]

print("Total de ventas:", calcular_total(ventas))
