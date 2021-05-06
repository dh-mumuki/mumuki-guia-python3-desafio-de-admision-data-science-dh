class Test248(unittest.TestCase):
  def test_248(self):
    self.assertEquals(stop_248([2, 3, 4, 248]), [2, 4])
    self.assertEquals(stop_248([2, 3, 4, 248, 6, 8, 10]), [2, 4, 6, 8, 10])
      
  def test_no_evens(self):
    self.assertEquals(stop_248([3, 5, 7]), [])

  def test_n_args(self):
    try:
      with self.assertRaises(TypeError):
        stop_248()
      with self.assertRaises(TypeError):
        stop_248([2, 4, 6, 248, 4], 2)
    except:
      raise ValueError("Revisar numero de argumentos de funcion.")