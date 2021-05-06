class TestCheck(unittest.TestCase):

  def test_four_in_list(self):
    self.assertTrue(check(4, [3, 2, 4, 5]), "check(4, [3, 2, 4, 5]) != True")
    
  def test_four_not_in_list(self):
    self.assertEqual(check(4, [3, 2, 5]), [3, 2, 5, 4], "check(4, [3, 2, 5]) != [3, 2, 5, 4]")

  def test_n_args(self):
    try:
      with self.assertRaises(TypeError):
        check()
      with self.assertRaises(TypeError):
        check(1, [1, 2, 3], 6)
    except:
      raise ValueError("Revisar numero de argumentos de funcion.")