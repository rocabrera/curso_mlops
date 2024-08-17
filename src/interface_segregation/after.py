from typing import Any
from abc import ABC, abstractmethod

class ModelStorage(ABC):
    @abstractmethod
    def add(self, filename: str, model: Any) -> str | None:
        pass 

class ExtraStorage(ABC):
    @abstractmethod
    def attach_ssd(self, qtd: int) -> str | None:
        pass 


class FileSystemModelStorage(ModelStorage, ExtraStorage):

    def attach_ssd(self, qtd: int):
        print(f"Adicionando {qtd} GB de espaço em disco")
        
class InMemoryModelStorage(ModelStorage):
    pass


