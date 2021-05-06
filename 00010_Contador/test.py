class TestFixtures(unittest.TestCase):
  def test_contador_2(self):
    self.assertEqual(cuenta_cuatro([1, 4, 6, 4, 7]), 2)
  def test_contado_3(self):
    self.assertEqual(cuenta_cuatro([1, 4, 6, 4, 4]), 3)
  def test_contado_0(self):
    self.assertEqual(cuenta_cuatro([1, 2, 3]), 0)
    
  def test_n_args(self):
    try:
      with self.assertRaises(TypeError):
        cuenta_cuatro()
      with self.assertRaises(TypeError):
        cuenta_cuatro([1, 2], 2)
    except:
      raise ValueError("Revisar numero de argumentos de funcion.")