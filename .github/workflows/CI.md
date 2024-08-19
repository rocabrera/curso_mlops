# name: Primeiro Workflow

# on:
#   pull_request:
#     branches: [ "main" ]

# jobs:
#   CI:
#     runs-on: ubuntu-latest

#     steps:

#       - name: Baixando repositório
#         uses: actions/checkout@v4

#       - name: Configurando Python
#         uses: actions/setup-python@v5
#         with:
#           # Semantic version range syntax or exact version of a Python version
#           python-version: '3.11'
#           # Optional - x64 or x86 architecture, defaults to x64
#           architecture: 'x64'
      
#       - name: Instalando as dependências
#         run: |
#           pip install -e .
#           pip install -r requirements-dev.txt

#       - name: Executando testes
#         run: pytest tests

#       - name: Linter
#         run: ruff check

#       - name: Aplicando pacote de segurança
#         run: bandit -c pyproject.toml -r .