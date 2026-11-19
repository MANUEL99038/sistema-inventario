
import unittest
from src.producto import Producto


class TestProducto(unittest.TestCase):

    def setUp(self):
        self.producto = Producto("Laptop", 12000, 5)

    def test_nombre_producto(self):
        self.assertEqual(self.producto.nombre, "Laptop")

    def test_precio_producto(self):
        self.assertEqual(self.producto.precio, 12000)

    def test_stock_producto(self):
        self.assertEqual(self.producto.stock, 5)

    def test_mostrar_producto(self):
        resultado = self.producto.mostrar()
        self.assertIn("Laptop", resultado)

    def test_valor_inventario(self):
        self.assertEqual(
            self.producto.calcular_valor_inventario(),
            60000
        )


if __name__ == "__main__":
    unittest.main()
