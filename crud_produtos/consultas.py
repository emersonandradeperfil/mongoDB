from crud_vendedores.conexao import db

produtos = db['tabela_de_produtos']
vendedores = db["tabela_de_vendedores"]
clientes = db["tabela_de_cliente"]
notas = db["notas_fiscais"]
itens = db["itens_notas_fiscais"]


# SELECT SABOR,
#        COUNT(*) AS TOTAL
# FROM TABELA_DE_PRODUTOS
# GROUP BY SABOR;

# consulta = [
#     {
#         "$group": {
#             "_id": "$SABOR",
#             "TOTAL": {
#                 "$sum": 1
#             }
#         }
#     }
# ]
# resultado = produtos.aggregate(consulta)
#
# for item in resultado:
#     print(item)
#----------------------------------------------------

# SELECT SABOR,
#        COUNT(*) AS TOTAL
# FROM TABELA_DE_PRODUTOS
# GROUP BY SABOR
# HAVING COUNT(*) > 2;

#consulta = [
#    {
#        "$group": {
#            "_id": "$SABOR",
#            "TOTAL": {
#                "$sum": 1
#            }
#        }
#    },
#    {
#        "$match": {
#            "TOTAL": {
#                "$gt": 2
#            }
#        }
#    }
#]
#resultado = produtos.aggregate(consulta)
#for item in resultado:
#    print(item)
#-----------------------------------------

# SELECT NF.MATRICULA,
#        TV.NOME,
#        COUNT(*) AS NUMERO_NOTAS
#
# FROM NOTAS_FISCAIS NF
#
# INNER JOIN TABELA_DE_VENDEDORES TV
# ON NF.MATRICULA = TV.MATRICULA
#
# GROUP BY NF.MATRICULA,
#          TV.NOME;

consulta = [
    {
        "$lookup": {
            "from": "tabela_de_vendedores",
            "localField": "MATRICULA",
            "foreignField": "MATRICULA",
            "as": "VENDEDOR"
        }
    },
    {
        "$unwind": "$VENDEDOR"
    },
    {
        "$group": {
            "_id": {
                "MATRICULA": "$MATRICULA",
                "NOME": "$VENDEDOR.NOME"
            },
            "NUMERO_NOTAS": {
                "$sum": 1
            }
        }
    },
    {
        "$project": {
            "_id": 0,
            "MATRICULA": "$_id.MATRICULA",
            "NOME": "$_id.NOME",
            "NUMERO_NOTAS": 1
        }
    }
]
resultado = notas.aggregate(consulta)


dados = list(resultado)


# for item in resultado:
#     print(item)

# for item in dados:
#
#     print(
#         f'MATRICULA: {item["MATRICULA"]} | '
#         f'NOME: {item["NOME"]} | '
#         f'NUMERO_NOTAS: {item["NUMERO_NOTAS"]}'
#     )











