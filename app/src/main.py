import json
import pickle
from src.loader import storage
from pydantic import BaseModel
from fastapi import FastAPI, Response, UploadFile

app = FastAPI()

class ModelParams(BaseModel):
    id: str
    features: list

@app.post("/model/upload")
async def model_upload(file: UploadFile):

    model = file.file.read()
    key: str | None =  storage.add(filename=file.filename, model=model)
    file.file.close()

    if key:
        response = {"message": "Modelo salvo com sucesso", "key": key}
        return  Response(content=json.dumps(response), media_type="application/json", status_code=201)
    else:
        response = {"message": "Problema no servidor"}
        return  Response(content=json.dumps(response), media_type="application/json", status_code=500)
        
@app.post("/model/predict")
async def model_upload(params: ModelParams):
    model =  storage.get(key=params.id)
   
    if model:
        model = pickle.loads(model)
        model_answer = model.predict([params.features])
        response = {
            "storage_used": storage.__class__.__name__,
            "data":{
                "model_answer": int(model_answer[0])
            }
        }
        return  Response(
            content=json.dumps(response), 
            media_type="application/json", 
            status_code=200
        )

    else:
        response={"message": "Modelo especificado não existe"}
        return  Response(
            content=json.dumps(response), 
            media_type="application/json", 
            status_code=400
        )

# TODO: Crie a rota para deletar modelos
# Lembre-se quando um problema acontecer seu usuário quer saber o motivo se possível

    
@app.get("/")
async def root():
    return {"message": "Healt Check"}