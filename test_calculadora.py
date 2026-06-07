import unittest
from Calculadora import potencia, raiz_cuadrada, sumar, restar, multiplicar, dividir

class TestCalculadora(unittest.TestCase):

    def test_sumar(self):
        self.assertEqual(sumar(3, 2), 5)

    def test_restar(self):
        self.assertEqual(restar(10, 4), 6)

    def test_multiplicar(self):
        self.assertEqual(multiplicar(3, 4), 12)

    def test_dividir(self):
        self.assertEqual(dividir(10, 2), 5)

    def test_dividir_por_cero(self):
        with self.assertRaises(ValueError):
            dividir(5, 0)
    def test_potencia(self):
        self.assertEqual(potencia(2, 3), 8)

    def test_raiz_cuadrada(self):
        self.assertEqual(raiz_cuadrada(9), 3.0)

    def test_raiz_negativa(self):
        with self.assertRaises(ValueError):
            raiz_cuadrada(-1)

if __name__ == '__main__':
    unittest.main()
