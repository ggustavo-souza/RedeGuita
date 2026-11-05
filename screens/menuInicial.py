import subprocess
from colorama import Style, init, Fore

# Inicia o colorama (biblioteca para colorir o texto no terminal)
init(autoreset=True)

def menuInicial(estadoMensagemErro: str):
    # Import dentro da função para evitar erro
    from model.buscaGuitarra import buscaGuitarra
    from screens.montarPerfilGuitarra import montarPerfilGuitarra

    # Declaração das variáveis essenciais
    resposta: int = 0
    # Futuramente fazer ele salvar em JSON (para garantir o estado do perfil de guitarra montado)
    perfilGuitarra: buscaGuitarra = buscaGuitarra() 

    subprocess.run(["clear"], shell=True)

    while(resposta != 3):
        print("Bem-vindo ao RedeGuita! Escolha as opções que deseja procurar:")
        print("------------------------------------------------")
        print(Style.BRIGHT + "1 - Montar perfil de guitarra")
        print(Style.BRIGHT + "2 - Realizar busca de guitarras")
        print(Style.BRIGHT + "3 - Sair do programa")

        print("------------------------------------------------")

        if(estadoMensagemErro != ""):
            print(Style.BRIGHT + Fore.RED + estadoMensagemErro)

        print('------------------------------------------------')

        resposta = int(input("Digite a opção desejada: "))


        match resposta:
            case 1:
                perfilGuitarra = montarPerfilGuitarra()
            case 2:
                if(perfilGuitarra and not perfilGuitarra.estaVazia()):
                    perfilGuitarra.buscarGuitarras()
                else:
                    novaMensagemErro = "Você precisa montar um perfil de guitarra antes de realizar a busca."
                    menuInicial(novaMensagemErro)
            case 3:
                print("Saindo do programa...")
                exit(0)
            case _:
                novaMensagemErro = "Opção inválida. Por favor, escolha uma opção válida."
                menuInicial(novaMensagemErro)

