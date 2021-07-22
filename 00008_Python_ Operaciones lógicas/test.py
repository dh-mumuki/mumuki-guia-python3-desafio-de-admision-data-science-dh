class TestFixtures(unittest.TestCase):
  
  def test_Si_10_devuelve_falso(self):
      self.assertFalse(check(10), "check(10) debe devolver False. Revisa los límites de las condiciones.")
      
  def test_Si_99_devuelve_falso(self):
      self.assertFalse(check(99), "check(99) debe devolver False. Revisa los límites de las condiciones.")
  
  def test_Si_100_devuelve_verdadero(self):
      self.assertTrue(check(100), "check(100) debe devolver True. Revisa los límites de las condiciones.")
      
  def test_Si_101_devuelve_verdadero(self):
      self.assertTrue(check(101), "check(101) debe devolver True. Revisa los límites de las condiciones.")
      
  def test_Si_387_devuelve_verdadero(self):
      self.assertTrue(check(387), "check(387) debe devolver True. Revisa los límites de las condiciones.")
  
  def test_Si_999_devuelve_verdadero(self):
      self.assertTrue(check(999), "check(999) debe devolver True. Revisa los límites de las condiciones.")
      
  def test_Si_1000_devuelve_verdadero(self):
      self.assertTrue(check(1000), "check(1000) debe devolver True. Revisa los límites de las condiciones.")
      
  def test_Si_1001_devuelve_falso(self):
      self.assertFalse(check(1001), "check(1001) debe devolver False. Revisa los límites de las condiciones.")
      
  def test_Si_2749_devuelve_falso(self):
      self.assertFalse(check(2749), "check(2749) debe devolver False. Revisa los límites de las condiciones.")   
  
  def test_Numero_de_argumentos(self):
    try:
      with self.assertRaises(TypeError):
        check()
      with self.assertRaises(TypeError):
        check(1, 2)
    except:
      raise ValueError("Revisar el numero de argumentos en la función.")

  def test_values(self):
    function = lambda x: x >= 100 and x <= 1000
    correct_values = [function(value) for value in range(0, 1100, 50)]
    tested_values = [check(value) for value in range(0, 1100, 50)]
    self.assertEqual(correct_values, tested_values)
