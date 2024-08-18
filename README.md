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


Tags:
``bash
git tag -a v0.0.1 -m "version 0.0.1"
```

``bash
git tag --delete <version>
```

