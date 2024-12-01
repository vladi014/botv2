
import unittest
from stats.estadistica import comprobar_cotizaciones, calcular_ganancia

class TestEstadistica(unittest.TestCase):

    def test_comprobar_cotizaciones_valid(self):
        result = comprobar_cotizaciones("1.5", "2.5", 100)
        self.assertTrue(result[0])
        self.assertGreater(result[1], 0)
        self.assertGreater(result[2], 0)

    def test_comprobar_cotizaciones_invalid(self):
        result = comprobar_cotizaciones("1.1", "1.1", 100)
        self.assertFalse(result[0])
        self.assertEqual(result[1], 0)
        self.assertEqual(result[2], 0)

    def test_calcular_ganancia_valid(self):
        ganancia = calcular_ganancia(1.5, 2.5, 60, 40)
        self.assertGreater(ganancia, 0)

    def test_calcular_ganancia_invalid(self):
        ganancia = calcular_ganancia(1.1, 1.1, 0, 0)
        self.assertEqual(ganancia, 0)

if __name__ == '__main__':
    unittest.main()
