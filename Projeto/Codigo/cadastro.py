import json
arquivo = "dados.json" 
dados = carregar_json

def carregar_json():
    with open(arquivo,"r", encoding="UTF-8") as file:
        return (json.load(file))

def salvar_dados(novo_user):
   with open(arquivo,"w", encoding="UTF-8") as file:
       json.dump(novo_user,file,indent=4,)


def cadastrar():
  dados == carregar_json()


while(True):
    print("=================")
    nome = str(input("Digite seu Nome:"))
    idade = int(input("Digite sua Idade:"))
    senha = str(input("Digite sua Senha:"))
    conf_senha = str(input("Confirme sua Senha:"))

    novo_user = {
       "Nome": str(nome),
       "Idade":int(idade),
       "Senha":str(senha)
    }

    if (senha == conf_senha):   
        dados.append(novo_user)
        salvar_dados(dados)
        print("cadastro Realizado ! ")
        break
    else: 
        print("Erro ! As senhas não coincidem. Tente novamente !")

cadastrar()