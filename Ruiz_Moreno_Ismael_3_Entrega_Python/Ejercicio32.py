precios = [10, 250, 30, 150, 80, 300]

contador = 0

for precio in precios:
    if precio > 100:
        print(precio, "€")
        contador = contador + 1

print("Productos con precio superior a 100 €:", contador)
