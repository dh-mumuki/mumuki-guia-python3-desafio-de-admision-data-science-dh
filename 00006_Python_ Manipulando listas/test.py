class Test(unittest.TestCase):

  def test_retorna_96374865_se_argumento_e_lista(self):
    self.assertEqual(soma_int(lista), 96374865, 'Deve retornar 96374865 se o argumento é a variável lista.')