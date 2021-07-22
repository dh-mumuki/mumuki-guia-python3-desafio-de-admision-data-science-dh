class TestFixtures(unittest.TestCase):
  
  def test_1001(self):
      self.assertFalse(check(1001), "El 1001 NO debe pasar.")

  def test_900(self):
      self.assertTrue(check(900), "El 900 debe pasar.")

  def test_100(self):
      self.assertTrue(check(100), "El 100 debe pasar.")

  def test_50(self):
      self.assertFalse(check(50), "El 50 NO debe pasar.")
  
  def test_n_args(self):
    try:
      with self.assertRaises(TypeError):
        check()
      with self.assertRaises(TypeError):
        check(1, 2)
    except:
      raise ValueError("Revisar numero de argumentos de funcion.")

  def test_values(self):
    function = lambda x: x >= 100 and x <= 1000
    correct_values = [function(value) for value in range(0, 1100, 50)]
    tested_values = [check(value) for value in range(0, 1100, 50)]
    self.assertEqual(correct_values, tested_values)
