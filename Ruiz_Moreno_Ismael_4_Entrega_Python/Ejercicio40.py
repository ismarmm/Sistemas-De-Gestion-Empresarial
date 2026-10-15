def aplicar_descuento(precio, descuento=0):
    cantidad_descuento = precio * descuento / 100
    precio_final = precio - cantidad_descuento
    return precio_final

print(aplicar_descuento(100))
print(aplicar_descuento(100, 10))
print(aplicar_descuento(250, 20))
