
class Producto:
    def __init__(self, codigo, nombre, precio, existencia):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.existencia = existencia

    def mostrar_informacion(self):
        print("===== INFORMACION DEL PRODUCTO =====")
        print("Codigo:", self.codigo)
        print("Nombre:", self.nombre)
        print("Precio: $", self.precio)
        print("Existencia:", self.existencia, "unidades")


# Crear un producto
producto1 = Producto("P001", "Teclado", 450.00, 15)

# Mostrar informacion del producto
producto1.mostrar_informacion()
