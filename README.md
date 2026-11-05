# RedeGuita

O RedeGuita é uma aplicação de linha de comando desenvolvida em Python para auxiliar na busca e monitoramento de ofertas de guitarras em diferentes plataformas online.

O programa permite que o usuário defina as características do instrumento que deseja encontrar (como marca, modelo, cor e limites de preço) e selecione os sites onde a pesquisa deve ser executada. Ao encontrar anúncios correspondentes, o sistema coleta as informações essenciais e os links de acesso, salvando os resultados em um arquivo .csv no diretório /repo.

## Sites Suportados

A ferramenta foi projetada para realizar buscas nas seguintes plataformas:

* Facebook Marketplace
* OLX
* Mercado Livre

## Funcionamento

1. O usuário inicia a aplicação pelo terminal.
2. Através do menu interativo, define os parâmetros da guitarra desejada (marca, modelo, cor, preço mínimo e preço máximo).
3. Seleciona as plataformas onde deseja executar a consulta.
4. O programa realiza a busca e extrai os dados dos anúncios encontrados.
5. Os links e detalhes coletados são gravados em uma planilha .csv dentro da pasta /repo para posterior consulta.

## Estrutura do Projeto

* app.py: Arquivo principal de inicialização da aplicação.
* model/: Contém as classes e regras de negócio relacionadas ao perfil e busca das guitarras.
* screens/: Módulos responsáveis pela exibição dos menus e interação com o usuário no terminal.
* services/: Funções de serviço, incluindo a persistência dos dados em formato .csv.
* repo/: Diretório onde os arquivos .csv gerados pelas buscas são armazenados.
* requirements.txt: Lista de dependências do projeto.

## Bibliotecas Utilizadas

O projeto faz uso das seguintes bibliotecas:

* Pandas: Manipulação de dados e exportação dos resultados para arquivo .csv.
* Requests: Envio de requisições HTTP para consulta das páginas e dados dos anúncios.
* Colorama: Formatação e estilização de mensagens e opções no terminal.

## Como Executar

### Pré-requisitos

* Python 3.10 ou superior instalado.

### Instalação

1. Clone o repositório ou faça o download dos arquivos:
```bash
git clone https://github.com/seu-usuario/RedeGuita.git
cd RedeGuita
```

2. Crie e ative um ambiente virtual:
```bash
# No Linux ou macOS:
python3 -m venv venv
source venv/bin/activate

# No Windows:
python -m venv venv
venv\Scripts\activate
```

3. Instale as dependências necessárias:
```bash
pip install -r requirements.txt
```

4. Inicie o programa:
```bash
python app.py
```
