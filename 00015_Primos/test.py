class TestPrimos(unittest.TestCase):
  def test_primos(self):
    self.assertTrue(primos(2))
    self.assertTrue(primos(3))
    self.assertTrue(primos(5))
    self.assertTrue(primos(7))
    self.assertTrue(primos(11))
    self.assertTrue(primos(13))
    self.assertTrue(primos(17))
    self.assertTrue(primos(19))

  def test_no_primo(self):
    self.assertFalse(primos(1))
    self.assertFalse(primos(4))
    self.assertFalse(primos(6))
    self.assertFalse(primos(8))
    self.assertFalse(primos(9))
    self.assertFalse(primos(10))
    self.assertFalse(primos(15))

  def test_n_args(self):
    try:
      with self.assertRaises(TypeError):
        primos()
      with self.assertRaises(TypeError):
        primos(1, 2)
    except:
      raise ValueError("Revisar numero de argumentos de funcion.")