import pickle
from typing import Any
from pathlib import Path
from abc import ABC, abstractmethod

class ModelStorage(ABC):
    @abstractmethod
    def add(self, filename: str, model: Any) -> str | None:
        pass 

    @abstractmethod
    def delete(self, key: str) -> bool:
        pass
    
    @abstractmethod
    def get(self, key: str) -> Any | None:
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

    def delete(self, key: str) -> bool:
        try:
            Path(key).unlink(missing_ok=True)
        except Exception as e:
            print(e)
            return False
        else:
            return True

    def get(self, key: str) -> Any | None:
        path = Path(key)
        if path.exists():
            with path.open(mode="rb") as f:
                return pickle.load(f)
            

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

    def delete(self, key: str) -> bool:
        try:
            del self.data[key]
        except Exception as e:
            print(e)
            return False
        else:
            return True

    def get(self, key: str) -> Any | None:
        return self.data.get(key, None) 