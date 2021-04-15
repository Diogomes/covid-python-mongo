import pymongo


myclient = pymongo.MongoClient("mongodb://root:MongoDB2021!@localhost:27017")

# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["banco-de-dados2"]
mycol = mydb["COVIDBR"]


# x = mycol.find_one()
# print(x)



def menuPrincipal():
	print("O que deseja fazer: ")
	print("1 - Pesquisar por sigla Maiuscula do estado.")
	print("2 - Pesquisar por municípios.")
	# print("3 - Pesquisar por quantidade de mortes acumuladas por estado.")
	print("9 - Sair")
	opcao = input("____________________________________________________________________________\n\n")

	if opcao == '1':
		pesquisar_estado()
		
	if opcao == '2':
		pesquisar_municipios()

	if opcao == '9':
		sair()



def pesquisar_municipios():
	municipio = input("Digite o município que deseja pesquisar: ")
	# cidade_formatada = '"{}"'.format(municipio)
	# m = '"municipio"'
	# consulta = "{" + '"municipio"' + ":"  +  cidade_formatada  + "}"
	# consulta = "municipio: " + municipio
	# print(consulta)
	listar_dados("municipio" , municipio)
  
def pesquisar_estado():
	sigla_estado = input("Digite a sigla que deseja pesquisar: ")
	# cidade_formatada = '"{}"'.format(municipio)
	# m = '"municipio"'
	# consulta = "{" + '"municipio"' + ":"  +  cidade_formatada  + "}"
	# consulta = "municipio: " + municipio
	# print(consulta)
	listar_dados("estado" , sigla_estado)

def pesquisar_obitos_acumulados_estado():
	sigla_estado = input("Digite a sigla do estado que deseja pesquisar a quantidade mortos: ")
	listar_dados_obitos("estado" , sigla_estado)


def sair():
	exit()



def listar_dados(colecao, valor):
	for b in mycol.find({colecao:valor}):
		print(b)


opcao = ''
while opcao != 9:
    menuPrincipal()




















# def listar_dados_obitos(colecao, valor):
# 	for b in mycol.({colecao:valor}, {colecao:obitosAcumulado}):
# 		print(b)


# // Requires official MongoShell 3.6+
# db = db.getSiblingDB("banco-de-dados2");
# db.getCollection("COVIDBR").aggregate(
#     [
#         { 
#             "$match" : { 
#                 "estado" : "PE"
#             }
#         }, 
#         { 
#             "$group" : { 
#                 "_id" : { 
#                     "municipio" : "$municipio"
#                 }, 
#                 "MAX(obitosAcumulado)" : { 
#                     "$max" : "$obitosAcumulado"
#                 }
#             }
#         }, 
#         { 
#             "$project" : { 
#                 "MAX(obitosAcumulado)" : "$MAX(obitosAcumulado)", 
#                 "municipio" : "$_id.municipio", 
#                 "_id" : NumberInt(0)
#             }
#         }
#     ], 
#     { 
#         "allowDiskUse" : true
#     }
# );