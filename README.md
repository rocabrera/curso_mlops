# Para desenvolvimento do pacote

```bash
pip install -r requirements-dev.txt
```

# Comandos utilizados

```bash
ruff check
```

```bash
ruff format
```

Seguranca da aplicacao:
```bash
bandit -c pyproject.toml -r .
```

```bash
bandit -c -q pyproject.toml -r .
```

Package commands:

```bash
python -m build
```

```bash
python -m twine upload --repository testpypi dist/*
```