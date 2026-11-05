import subprocess

def montarPerfilGuitarra():
    from model.buscaGuitarra import buscaGuitarra

    subprocess.run(["clear"], shell=True)

    # Instância do perfil da guitarra a ser montada
    perfilGuitarra = buscaGuitarra()

    # Solicita ao usuário as informações para montar o perfil da guitarra
    perfilGuitarra.marca = input("Digite a marca da guitarra: ")

    perfilGuitarra.minPreco = float(input("Digite o preço mínimo: "))
    perfilGuitarra.maxPreco = float(input("Digite o preço máximo: "))

    perfilGuitarra.cor = input("Digite a cor da guitarra: ")

    perfilGuitarra.modelo = input("Digite o modelo da guitarra: ")

    # Retorna o perfil da guitarra montado em objeto da classe buscaGuitarra
    return perfilGuitarra