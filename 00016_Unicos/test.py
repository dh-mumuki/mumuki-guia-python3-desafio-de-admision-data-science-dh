class TestUnicosDos(unittest.TestCase):
  def test_unicos(self):
    self.assertEquals(lista_de_unicos([1, 2, 3, 3, 3, 3, 4, 5]), [1, 2, 3, 4, 5])
      
  def test_order(self):
    self.assertEquals(lista_de_unicos([1, 3, 3, 3, 3, 2, 4, 5]), [1, 2, 3, 4, 5])
      
  def test_n_args(self):
    try:
      with self.assertRaises(TypeError):
        lista_de_unicos()
      with self.assertRaises(TypeError):
        lista_de_unicos([2, 4, 6, 248, 4], 2)
    except:
      raise ValueError("Revisar numero de argumentos de funcion.")
