class Test(unittest.TestCase):

  def test_deve repetir_2_vezes_por_padrao(self):
    self.assertEqual(repete('Aa', 2), 'AaAa')

  def test_deve repetir_5_vezes_por_padrao(self):
    self.assertEqual(repete('Aa'), 'AaAaAaAaAa')
    
  def test_deve repetir_3_vezes_por_padrao(self):
    self.assertEqual(repete('Olá! ', 3), 'Olá! Olá! Olá! ')
    
  def test_deve repetir_3_vezes_por_padrao(self):
    self.assertEqual(repete('Olá! '), 'Olá! Olá! Olá! Olá! Olá! ')
    
    
    
  
