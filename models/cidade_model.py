from pydantic import BaseModel
from sqlalchemy import Column, String

from models.abstract_model import AbstractModel
from config.base import Base

class Cidade(Base, AbstractModel):
    __tablename__ = 'cidade'
    nome = Column(String)
    uf = Column(String)

    
    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'uf': self.uf,
        }
    
class CidadeInsert(BaseModel, AbstractModel):
    nome: str
    uf: str

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'uf': self.uf,
        }