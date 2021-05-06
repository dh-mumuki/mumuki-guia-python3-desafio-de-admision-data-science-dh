class TestFixtures(unittest.TestCase):
  def test_cuadrados(self):
    self.assertTrue(cuadrados() == [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729, 784, 841, 900])

  def test_n_args(self):
    try:
      with self.assertRaises(TypeError):
        cuadrados(1)
    except:
      raise ValueError("Revisar numero de argumentos de funcion.")
