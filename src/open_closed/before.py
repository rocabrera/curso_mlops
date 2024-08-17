from pathlib import Path
from typing import Any
import pickle

class ModelStorage():

    def __init__(self, storage_type: str) -> None:
    
        self.data = {}
        self.storage_type = storage_type 

    def add(self, filename: str, model: Any) -> Any:
        if self.storage_type == 'filesystem':
            try:
                path = (Path("tmp") / filename)
                path.parent.mkdir(parents=True, exist_ok=True)
                with path.open(mode="wb") as f:
                    pickle.dump(model, f)

            except Exception as e:
                print(e)
                return None
            else:
                return str(path)
            
        elif self.storage_type == 'inmemory':
            self.data[filename] = model

        else:
            raise ValueError("Invalid storage type")
        

