# Alterando um documento (posts) do banco de dados "bancoteste"
import pprint
import pymongo

# Conecta ao servidor MongoDB Atlas no endereço da nuvem
cliente = pymongo.MongoClient('mongodb+srv://eberbrea:TCbMH6Fj6FzG7YSb@cluster0.hanztba.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')

db = cliente.bancoteste                 # Acessa o banco de dados chamado 'bancoteste'
con = db.posts                          # conecta ao banco de dados

alterar_documento = con.update_one(
    {'author': 'Mike'},                 # Filtro
    {'$set':  {'title': "MongoDB isn't difficult!"}}        # Atualização
)

for p in con.find():                    # imprime todos os documentos/objetos (registros)
    pprint.pprint(p)
    print()

