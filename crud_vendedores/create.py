from crud_vendedores.conexao import db

produtos = db['tabela_de_produtos']

novo_produto = {
    'CODIGO_DO_PRODUTO':99999,
    'NOME_DO_PRODUTO':'Produto Teste',
    'SABOR': 'Pera',
    'PRECO_DE_LISTA': 8.50
}
produtos.insert_one(novo_produto)

print('Produto inserido com sucesso')