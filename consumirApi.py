#Faz a importacao das bibliotecas nescessarias
from pymongo import MongoClient
import requests, json

#define a url onde da api - Estatística
url_estatistica='https://covid-193.p.rapidapi.com/statistics?country=brazil'

#define a chave de permissao para consulta da api
headers = {
    'x-rapidapi-key': "44930f33f7msh6e4931973667a1dp1241fajsn04db830e6385",
    'x-rapidapi-host': "covid-193.p.rapidapi.com"
    }

#cria a conexao com a API
Dados_estatistica = requests.request("GET", url_estatistica, headers=headers)

#Converter o resposta da API de Texto para Json
Dados_json=json.loads(Dados_estatistica.text)

#Estancia a conexão com banco de dados
MinhaConexao=MongoClient("mongodb://root:MongoDB2021!@localhost:27017")


#Informa qual o Banco
Banco=MinhaConexao["covid"]


##Coleções ou (Collections) estão para o mongodb como tabelas estão para bancos relacionais
Colecoes=Banco.Brasil

##Checando se a conexão foi realizada
serverStatusResult=Banco.command("serverStatus")


#Fazendo o insert
if isinstance(Dados_json, list):
    #Para o caso do dicionário tiver mais de um Documento
    Colecoes.insert_many(Dados_json)
else:
    #Para o caso do dicionário tiver apenas um Documento
    Colecoes.insert_one(Dados_json)

