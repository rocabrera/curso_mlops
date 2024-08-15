## Develop API
fastapi dev src/main.py 

# Run Docker

- docker build -t application .
- docker container run -it --rm application bash


## Post command:
curl -d '{"id": "tmp/dt.pickle", "features": [0.1, 0.2, 0.07, 0.14]}' -H "Content-Type: application/json" -X POST http://127.0.0.1:8000/model/predict

