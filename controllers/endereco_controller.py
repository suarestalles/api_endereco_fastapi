from models.endereco_model import Endereco, EnderecoInsert
from repositories.endereco_repository import EnderecoRepository

class EnderecoController:

    def listAll(self, filtros) -> list[dict]:
        
        try:
            result = EnderecoRepository().listAll(filtros)
            return result
        except Exception as e:
            raise e
        
    def findById(self, id) -> Endereco:
        
        try:
            result = EnderecoRepository().findById(id)
            return result
        except Exception as e:
            raise e
        
    def findByCidadeId(self, id_cidade) -> list[dict]:
        
        try:
            result = EnderecoRepository().findByCidadeId(id_cidade)
            return result
        except Exception as e:
            raise e
        
    def insert(self, newEndereco: EnderecoInsert) -> str:
        
        try:
            result = EnderecoRepository().insert(newEndereco)
            return result
        except Exception as e:
            raise e
        
    def update(self, endereco_id: int, newEndereco: EnderecoInsert) -> dict:
        
        try:
            result = EnderecoRepository().update(endereco_id, newEndereco)
            return result
        except Exception as e:
            raise e
        
    def delete(self, endereco_id: int) -> str:
        
        try:
            return EnderecoRepository().delete(endereco_id)
        except Exception as e:
            raise e