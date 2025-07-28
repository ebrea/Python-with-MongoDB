# Consultando os documentos (posts) do banco de dados "bancoteste"
from datetime import date, datetime
import pprint
import pymongo
from pymongo import MongoClient

# Conecta ao servidor MongoDB Atlas no endereço da nuvem
cliente = pymongo.MongoClient('mongodb+srv://eberbrea:TCbMH6Fj6FzG7YSb@cluster0.hanztba.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')

db = cliente.bancoteste                 # Acessa o banco de dados chamado 'bancoteste'
con = db.posts                          # conecta ao banco de dados

# for p in con.find():                    # imprime todos os documentos/objetos (registros)
#     pprint.pprint(p)
#     print()

print('Total de Documentos:', con.count_documents({}))  # quantidade de documentos (posts/registros)
documento_selecionado = con.find_one({'author':'Patrícia'})   # Ele para no documento selecionado
pprint.pprint(documento_selecionado)
print()
tag1 = documento_selecionado['tags']
print(tag1)                                 # ['Python', 'MongoDB', 'SQL', 'html']

print(f'\n*** Estou estudando {tag1[1]} com Python ***')   # *** Estou estudando MongoDB com Python ***

data = documento_selecionado['date'].strftime('%d/%m/%Y')
print(f' Este documento foi postado dia {data}')


# print(con.count_documents({'tags':'MongoDB'}))     # quantidade de documentos cujas "tags" tem "MongoDB"

# for p in con.find().sort('author'): # imprime todos os documentos por ordem de "author"
#     print()
#     pprint.pprint(p)


# resultado = db.profiles.create_index([('author', pymongo.ASCENDING)])       # author_1
# print(sorted(list(db.profiles.index_information())))        # ['_id_', 'author_1']


'''
{'_id': ObjectId('6886ae68392603f04e165493'),
 'author': 'Patrícia',
 'date': datetime.datetime(2025, 7, 27, 19, 55, 36, 815000),
 'tags': ['Python', 'MongoDB', 'SQL', 'html'],
 'text': 'O Palmeiras NÂO tem Mundial'}
 
'''