clientes_tienda_a = {"Ana", "Luis", "Marta", "Carlos"}
clientes_tienda_b = {"Marta", "Carlos", "Lucía"}

# 1. Todos los clientes
todos = clientes_tienda_a | clientes_tienda_b

# 2. Clientes que están en ambas tiendas
ambas = clientes_tienda_a & clientes_tienda_b

# 3. Clientes únicamente de la tienda A
solo_a = clientes_tienda_a - clientes_tienda_b

print("Todos los clientes:", todos)
print("En ambas tiendas:", ambas)
print("Solo en tienda A:", solo_a)