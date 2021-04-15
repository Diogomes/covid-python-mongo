import pymongo

myclient = pymongo.MongoClient("mongodb://root:MongoDB2021!@localhost:27017")
mydb = myclient["banco-de-dados2"]
mycol = mydb["COVIDBR"]


def menuPrincipal():
	print("O que deseja fazer: ")
	print("1 - Pesquisar por mortes acumuladas de todos por estado.")
	print("2 - Pesquisar por mortes acumuladas por município.")
	print("3 - Inserir dados na Base de Dados.")
	print("9 - Sair")
	opcao = input("____________________________________________________________________________\n\n")

	if opcao == '1':
		pesquisar_estado()
		
	if opcao == '2':
		pesquisar_municipios()
	
	if opcao == '3':
		inserir_dados()

	
	if opcao == '9':
		sair()


def pesquisar_municipios():
	municipio = input("Digite o município que deseja pesquisar: ")
	listar_obitos_municipio("municipio" , municipio)
  
def pesquisar_estado():
	sigla_estado = input("Digite a sigla que deseja pesquisar: ")
	listar_obitos_estado("estado" , sigla_estado)

def pesquisar_obitos_acumulados_estado():
	sigla_estado = input("Digite a sigla do estado que deseja pesquisar a quantidade mortos: ")
	listar_dados_obitos("estado" , sigla_estado)

def inserir_dados():
	estados = input("Qual estado deseja adicionar: ")
	municipios = input("Qual munícipio deseja adicionar: ")
	datas = input("Informe a data a ser adicionada: ")
	obitosAcumulados = input("Digite a quantidade óbitos acumulados desta cidade: ")

	mycol.insert({"municipio": municipios, "estado": estados, "obitosAcumulado": obitosAcumulados , "data": datas})


# Conversão dos dados num dicionário
def listar_obitos_estado(colecao, valor):
	lista = {}
	for b in mycol.find({colecao:valor}):
		print(b["estado"] + " --- " + b["data"] + " --- " + b["obitosAcumulado"])


def listar_obitos_municipio(colecao, valor):
	lista = {}
	for b in mycol.find({colecao:valor}):
		print(b["municipio"] + " --- " + b["data"] + " --- " + b["obitosAcumulado"])


def sair():
	exit()

opcao = ''
while opcao != 9:
    menuPrincipal()