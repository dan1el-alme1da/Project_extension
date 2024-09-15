# Project_Extension
 
# IBHJ_Database

O projeto **IBHJ_Database** é uma aplicação web desenvolvida com Flask e PostgreSQL para gerenciar despesas administrativas. O sistema permite a inserção, edição, exclusão e visualização de registros de despesas.

## Estrutura do Projeto

- **app.py**: O arquivo principal do aplicativo Flask que contém a lógica para interação com o banco de dados e gerenciamento das rotas.
- **index.html**: O arquivo de template HTML que exibe a interface do usuário para a adição, edição e visualização de despesas.
- **static/**: Diretório contendo arquivos estáticos, como CSS e imagens.
- **templates/**: Diretório contendo arquivos de templates HTML (neste caso, apenas `index.html`).

## Requisitos

- Python 3.8 ou superior
- Flask
- psycopg2
- PostgreSQL

## Instalação

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/dan1el-alme1da/Project_extension.git
   cd IBHJ_Database

# Instale as dependências:
Crie um ambiente virtual e instale as dependências necessárias:

python -m venv venv
source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
pip install -r requirements.txt

Certifique-se de ter um banco de dados PostgreSQL em execução e configure a conexão no código app.py (alterando user, password, host, port e database conforme necessário).

# Execute o Servidor:
python app.py

A aplicação estará disponível em http://127.0.0.1:5000


