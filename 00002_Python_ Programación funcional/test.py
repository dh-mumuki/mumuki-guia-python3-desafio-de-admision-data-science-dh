class Test(unittest.TestCase):

  def test_si_sumar_3_al_doble_de_7_resulta_en_17(self):
    f = lambda x: 2*x
    g = lambda x: x + 3
    
    self.assertEqual(composicion(7,f,g), 17, "(7*2)+3 es distinto de 17!"))
    
  def test_si_sumar_4_al_triple_de_10_resulta_en_34(self):
    f = lambda x: 3*x
    g = lambda x: x + 4
    
    self.assertEqual(composicion(10,f,g), 34, "(10*4)+4 es distinto de 34!")
    
  def test_si_la_raiz_cuadrada_despues_de_dividir_128_por_2_resulta_en_8(self):
    from math import sqrt
    f = lambda x: x/2
    g = lambda x: sqrt(x)
    
    self.assertAlmostEqual(composicion(128,f,g), 8, "La raíz cuadrada de (128/2) es distinta de 8!")