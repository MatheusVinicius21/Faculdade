import json
import cadastro

arquivo = "dados_json"

def carregar_json():
    with open(arquivo,r,encoding="UTF-8") as file:
      return json.load(file)

def logar():
    dados == carregar_json()

    while(True):
        print("================")

usuario = str(input("usuário:")) 
senha = str(input("senha:"))
print("============")

login = False

for informacao in dados:
    if(usuario == informacao['nome'] and senha == informacao['senha']):
        login = True
        print("login realizado")

        if login:
            break
        else:
            resp = str(input("Erro de credenciais ! Deseja continuar [S/N] ")).upper()
            if (resp == "SIM" or resp == "S"):
                cadastro.cadastrar()
                dados = carregar_json()
            else:
                break

        




