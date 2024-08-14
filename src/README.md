# Machine Learning Communication

Esse pacote tem somente fins didáticos.


Instalar em modo desenvolvedor
- > pip install -e .

Build do pacote:
- > pip install -U build
- > python -m build

Publicar pacote:
- > pip install -U twine
- > twine check dist/*
- > python -m twine upload --repository testpypi dist/*

Instalar pacote:

- >pip install --index-url https://test.pypi.org/simple/ <package-name>

Versionando pacote com Git Tags:

- > git tag -a v0.0.1 -m "version 0.0.1"
- > git tag --delete <version>