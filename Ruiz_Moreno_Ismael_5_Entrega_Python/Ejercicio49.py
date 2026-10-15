class Producto:
    def __init__(self, codigo, nombre, precio, stock):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def mostrar_info(self):
        print(self.codigo, "-", self.nombre, "-", self.precio, "€ - Stock:", self.stock)

    def reponer(self, cantidad):
        self.stock = self.stock + cantidad


producto = Producto("P001", "Monitor", 199.99, 5)

print("Stock inicial:", producto.stock)
print("Reposición: 3")

producto.reponer(3)

print("Stock final:", producto.stock)
