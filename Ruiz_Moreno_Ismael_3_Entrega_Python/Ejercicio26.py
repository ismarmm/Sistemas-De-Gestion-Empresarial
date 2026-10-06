clientes_tienda_a = {"Ana", "Luis", "Marta", "Carlos"}
clientes_tienda_b = {"Marta", "Carlos", "Lucía"}

todos = clientes_tienda_a | clientes_tienda_b
ambas = clientes_tienda_a & clientes_tienda_b
solo_a = clientes_tienda_a - clientes_tienda_b

print("Todos los clientes:", todos)
print("Clientes en ambas tiendas:", ambas)
print("Clientes solo en tienda A:", solo_a)
