import inspect

class TestImpares(unittest.TestCase):

  def test_description_example(self):
    self.assertEqual(impares(21), [1,3,5,7,9,11,13,15,17,19])
    self.assertEqual(impares(18), [1,3,5,7,9,11,13,15,17])
    
  def test_listcomp(self):
    self.assertRegexpMatches(inspect.getsource(impares), r"\[.*for.*in.*\]", msg="El ejercicio debe resolverse con una lista por comprension.")

  def test_n_args(self):
    try:
      with self.assertRaises(TypeError):
        impares()
      with self.assertRaises(TypeError):
        impares(3, 2)
    except:
      raise ValueError("Revisar numero de argumentos de funcion.")
