from conexao import db

vendedores = db['tabela_de_vendedores']

novo_vendedor = {
    'MATRICULA':2387,
    'NOME':'Emerson de Andrade',
    'PERCENTUAL_COMISSAO':0.08,
    'DATA_ADMISSAO': '2014-08-15T00:00:00.000+00:00',
    'DE_FERIAS': 0,
    'BAIRRO':"Penha"
}
vendedores.insert_one(novo_vendedor)

print('Produto inserido com sucesso')

