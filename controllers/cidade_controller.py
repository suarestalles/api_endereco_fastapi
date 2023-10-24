from models.cidade_model import Cidade, CidadeInsert
from repositories.cidade_repository import CidadeRepository

class CidadeController:

    def listAll(self, filtros) -> list[dict]:
        
        try:
            result = CidadeRepository().listAll(filtros)
            return result
        except Exception as e:
            raise e
        
    def findById(self, id) -> Cidade:
        
        try:
            result = CidadeRepository().findById(id)
            return result
        except Exception as e:
            raise e
        
    def insert(self, newCidade: CidadeInsert) -> str:
        
        try:
            result = CidadeRepository().insert(newCidade)
            return result
        except Exception as e:
            raise e
        
    def update(self, cidade_id: int, newCidade: CidadeInsert) -> dict:
        
        try:
            result = CidadeRepository().update(cidade_id, newCidade)
            return result
        except Exception as e:
            raise e
        
    def delete(self, cidade_id: int) -> str:
        
        try:
            return CidadeRepository().delete(cidade_id)
        except Exception as e:
            raise e