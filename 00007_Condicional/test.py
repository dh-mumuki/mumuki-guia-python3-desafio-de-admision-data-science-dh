class TestFixtures(unittest.TestCase):
  def test_uno_esta_bien(self):
      self.assertEquals(difference(14), 3)
      self.assertEquals(difference(-11), 28)
  
  def test_dos_esta_bien(self):
      self.assertEquals(difference(22), 10)