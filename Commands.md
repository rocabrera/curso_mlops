## Develop API
fastapi dev src/main.py 

# Docker

Builda imagem
> docker build -t application .

Executa aplicação:
> docker container run -p 8000:8000 --rm application

Modo iterativo:
> docker container run -it --rm application bash


## Post command:

```bash
curl -d '{"id": "tmp/dt.pickle", "features": [0.1, 0.2, 0.07, 0.14]}' -H "Content-Type: application/json" -X POST http://127.0.0.1:8000/model/predict
```

https://fastapi.tiangolo.com/fastapi-cli/