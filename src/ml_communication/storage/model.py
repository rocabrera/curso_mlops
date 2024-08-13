import pickle
from typing import Any
from pathlib import Path
from abc import ABC, abstractmethod

class ModelStorage(ABC):
    @abstractmethod
    def add(self, path: Path, model: Any) -> bool:
        pass
    

    @abstractmethod
    def delete(self, path: Path) -> bool:
        pass
    
    @abstractmethod
    def get(self, path: Path) -> Any | None:
        pass


class FileSystemModelStorage(ModelStorage):

    def add(self, path: Path, model: Any) -> bool:
        try:
            with path.open(mode="wb") as f:
                pickle.dump(model, f)

        except Exception as e:
            print(e)
            return False
        else:
            return True

    def delete(self, path: Path) -> bool:
        try:
            path.unlink(missing_ok=True)

        except Exception as e:
            print(e)
            return False
        else:
            return True

    def get(self, path: Path) -> Any | None:
        if path.exists():
            with path.open(mode="rb") as f:
                return pickle.load(f)
            

class InMemoryModelStorage(ModelStorage):
    def __init__(self):
        self.data = {}

    def add(self, path: Path, model: Any) -> bool:
        try:
            self.data[path] = model
        except Exception as e:
            print(e)
            return False
        else:
            return True

    def delete(self, path: Path) -> bool:
        try:
            del self.data[path]
        except Exception as e:
            print(e)
            return False
        else:
            return True

    def get(self, path: Path) -> Any | None:
        return self.data.get(path, None) 