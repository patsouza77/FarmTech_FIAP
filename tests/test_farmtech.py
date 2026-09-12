"""Testes automatizados dos cálculos principais da FarmTech."""

import sys
import unittest
from pathlib import Path


RAIZ_PROJETO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ_PROJETO))

from farmtech import (  # noqa: E402
    calcular_area_retangulo,
    calcular_area_trapezio,
    calcular_fertilizante_kg,
    calcular_herbicida_litros,
    criar_registro_milho,
    criar_registro_soja,
)


class TestCalculosFarmTech(unittest.TestCase):
    def test_area_retangulo(self):
        area_m2, area_ha = calcular_area_retangulo(100, 50)
        self.assertEqual(area_m2, 5_000)
        self.assertEqual(area_ha, 0.5)

    def test_area_trapezio(self):
        area_m2, area_ha = calcular_area_trapezio(120, 80, 100)
        self.assertEqual(area_m2, 10_000)
        self.assertEqual(area_ha, 1.0)

    def test_herbicida_em_litros(self):
        resultado = calcular_herbicida_litros(20, 100, 2)
        self.assertEqual(resultado, 4.0)

    def test_fertilizante_em_quilos(self):
        resultado = calcular_fertilizante_kg(1.25, 200)
        self.assertEqual(resultado, 250.0)

    def test_registro_soja(self):
        registro = criar_registro_soja(1, "S-01", 100, 50, 20, 100, 2)
        self.assertEqual(registro["cultura"], "Soja")
        self.assertEqual(registro["area_hectares"], 0.5)
        self.assertEqual(registro["quantidade_insumo"], 4.0)
        self.assertEqual(registro["unidade_insumo"], "litros")

    def test_registro_milho(self):
        registro = criar_registro_milho(2, "M-01", 120, 80, 100, 250)
        self.assertEqual(registro["cultura"], "Milho")
        self.assertEqual(registro["area_hectares"], 1.0)
        self.assertEqual(registro["quantidade_insumo"], 250.0)
        self.assertEqual(registro["unidade_insumo"], "kg")


if __name__ == "__main__":
    unittest.main()
