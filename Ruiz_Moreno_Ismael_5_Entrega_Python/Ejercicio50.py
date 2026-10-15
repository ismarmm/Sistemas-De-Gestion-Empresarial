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

    def vender(self, cantidad):
        if cantidad <= 0:
            print("Cantidad no válida")
        elif cantidad <= self.stock:
            self.stock = self.stock - cantidad
            print("Venta realizada")
        else:
            print("Stock insuficiente")


producto = Producto("P001", "Monitor", 199.99, 8)

producto.mostrar_info()
producto.vender(3) 
producto.mostrar_info()
