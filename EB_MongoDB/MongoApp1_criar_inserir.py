# Cria um banco de dados MongoDB Atlas (na nuvem) e insere um documento (registro)
import datetime
import pprint
import pymongo                                      # ou inclui: "as pyM" para abreviar

# Conecta ao servidor MongoDB Atlas no endereço da nuvem
cliente = pymongo.MongoClient('mongodb+srv://eberbrea:TCbMH6Fj6FzG7YSb@cluster0.hanztba.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')

db = cliente.bancoteste           # Acessa o banco de dados chamado 'bancoteste'
con = db.posts                      # Acessa ou cria a conexão "conexao" (ou conexao = db.bancoteste)
# print(conexao)
doc1 = {                            # Documento a ser inserido na coleção
    "author": "Maria",
    "text": "Treinando o MongoDB",
    "title": "Vai Timão",
    "date": datetime.datetime.now(),
}

id_gerado = con.insert_one(doc1).inserted_id     # Insere o documento e obtém o id gerado
# print(con.find_one({"_id": id_gerado}))          # ou  print(id_gerado)

pprint.pprint(con.find_one({"_id": id_gerado}))   # mais organizado (um abaixo do outro). Imprime apenas o primeiro documento
print('')

# pprint.pprint(con.find_one({'author': 'Maria'}))    # imprime só o documento (objeto) selecionado

'''
* Insere um documento doc1 na coleção colecao1  e armazena o ID gerado automaticamente do 
novo documento na variável id_gerado

'''