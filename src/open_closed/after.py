import pickle
from typing import Any
from pathlib import Path
from abc import ABC, abstractmethod

class ModelStorage(ABC):
    @abstractmethod
    def add(self, filename: str, model: Any) -> str | None:
        pass 

class FileSystemModelStorage(ModelStorage):

    def add(self, filename: Path, model: Any) -> str | None:
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
        
class InMemoryModelStorage(ModelStorage):
    def __init__(self):
        self.data = {}

    def add(self, filename: str, model: Any) -> str | None:
        try:
            self.data[filename] = model
        except Exception as e:
            print(e)
            return None
        else:
            return filename


