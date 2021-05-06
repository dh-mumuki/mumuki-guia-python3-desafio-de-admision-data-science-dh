class Test(unittest.TestCase):

  def test_retorna_48_se_argumento_e_10(self):
    self.assertEqual(soma_pares_em_pi(10), 48, 'Deve retornar 48 se o argumento é 10.')

  def test_retorna_5166_se_argumento_e_1251(self):
    self.assertEqual(soma_pares_em_pi(1251), 5166, 'Deve retornar 5166 se o argumento é 1251.')
    
  def test_retorna_2618_se_argumento_e_650(self):
    self.assertEqual(soma_pares_em_pi(650), 2618, 'Deve retornar 2618 se o argumento é 650.')
    
  def test_retorna_148_se_argumento_e_35(self):
    self.assertEqual(soma_pares_em_pi(35), 148, 'Deve retornar 148 se o argumento é 35')
    
  def test_retorna_1484_se_argumento_e_372(self):
  self.assertEqual(soma_pares_em_pi(372), 1484, 'Deve retornar 1484 se o argumento é 372')