Uma loja tem a seguinte regra: quando um produto ficar abaixo de 18 unidades no estoque, é necessário fazer um novo pedido. O estoque da loja é guardado em um dicionário e é necessário desmembra-lo em duas listas.
Conside o seguinte código para informar ao gerente a necessidade de compras:

estoque_loja = {
    'Balde': 7,
    'Vassoura': 38,
    'Rodo': 22,
    'Esfregão': 59,
    'Aspirador': 44,
    'Sacos Plásticos': 12
}


produtosComEstoque = []
produtosParaReposicao = []

while len(estoque_loja) >= 0:
    itens = list(estoque_loja.keys())
    item = itens[0]
    
    if estoque_loja[item] >= 18:
        produtosComEstoque.append(item)
    else 
        produtosParaReposicao.append(item)
    del estoque_loja[item]
    
Assinale os problemas do código: