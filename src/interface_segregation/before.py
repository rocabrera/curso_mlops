from typing import Any
from abc import ABC, abstractmethod

class ModelStorage(ABC):
    @abstractmethod
    def add(self, filename: str, model: Any) -> str | None:
        pass 

    @abstractmethod
    def attach_ssd(self, qtd: int) -> str | None:
        pass 


class FileSystemModelStorage(ModelStorage):

    def attach_ssd(self, qtd: int):
        print(f"Adicionando {qtd} GB de espaço em disco")
        
class InMemoryModelStorage(ModelStorage):

    def attach_ssd(self, qtd: int):
        raise NotImplementedError(
            "Essa funcionalidade não é suportada por esse tipo de armazenamento"
        )



