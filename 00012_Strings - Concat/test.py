class TestConcat(unittest.TestCase):

  def test_concat_list(self):
    ls = ["a", "s", "d", "f"]
    self.assertEqual(
      concat_string(ls),
      "asdf",
      "concat_string(['a', 's', 'd', 'f']) != 'asdf'"
    )

  def test_not_iterable(self):
    with self.assertRaises(TypeError, msg="Tiene que fallar con un número"):
      concat_string(234)

  def test_n_args(self):
    try:
      with self.assertRaises(TypeError):
        concat_string()
      with self.assertRaises(TypeError):
        concat_string(["a", "s", "d"], 2)
    except:
      raise ValueError("Revisar numero de argumentos de funcion.")