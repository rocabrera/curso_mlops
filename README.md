# Aula 5 - Pacotes


## Setup

Visando evitar conflitos  entre dependencias de outros projetos python vamos criar um ambiente virtual. Uma das forma de fazer isso é utilizando o seguinte comando:

```bash
python -m venv <env_name>
```

Para entrar no ambiente virtual voce pode utilizar o comando (Mac ou Linux): 

```bash
source <env_name>/bin/activate
```

## Pyproject

A partir da PEP 621 a comunidade Python estabeleceu o uso do arquivo pyproject.toml como o jeito padrão de especificar metadados de um projeto. O arquivo [pyproject.toml](src/pyproject.toml) é separado por seções, denominadas tabelas ([build-system] e [project]).

A tabela [build-system] é utilizada para declarar qual backend (ferramenta) de construção vai ser utilizado para construir o pacote (nessa aula vamos utilizar o setuptools que normalmente ja vem instalado em ambientes virtuias). Além disso, você também pode passar dependências específicas para construção do seu pacote.

A tabela [project] é o formato que a maioria dos backends de construção utiliza para especificar os metadados básicos do seu projeto, por exemplo: nome, autores, dependências, entre outros.

Além disso, também existe uma tabela específica denominada [tool], que possui sub-tabelas específicas para cada ferramenta, por exemplo [tool.bandit], [tool.ruff], [tool.pytest.ini_options], entre outros.

## Instalando o pacote

Colocar na raiz do repositório o folder ```src``` e dentro o folder com o seu pacote (no nosso caso ```interface_communication```) é um padrão utilizado na industria.

Perceba que o nome do folder do seu pacote representa a forma como voce vai importar ele:, no nosso caso:

```python
import interface_communication
```

Durante a fase de desenvolvimento do seu pacote instale ele no modo editável (voce precisa estar no mesmo folder do arquivo ```pyproject.toml```):
```bash
pip install -e .
```

Caso voce nao esteja no folder correto voce vai receber um erro parecido com esse:
```bash
ERROR: file:///<path> does not appear to be a Python project: neither 'setup.py' nor 'pyproject.toml' found.
```




Git suporta dois tipos de tags: ```lightweight``` e ```annotated```.

Uma tag leve é muito parecida com um branch que não muda — é apenas um ponteiro para um commit específico.

Tags anotadas, no entanto, são armazenadas como objetos completos no banco de dados do Git.

```