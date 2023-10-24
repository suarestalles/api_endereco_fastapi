from pydantic import BaseModel
from sqlalchemy import Column, String, Integer, ForeignKey

from config.base import Base
from models.abstract_model import AbstractModel

class Endereco(Base, AbstractModel):
    __tablename__ = 'endereco'
    logradouro = Column(String)
    complemento = Column(String)
    bairro = Column(String)
    cep = Column(String)
    cidade_id = Column(Integer, ForeignKey('cidade.id'))

    def to_dict(self):
        return {
            'id': self.id,
            'logradouro': self.logradouro,
            'complemento': self.complemento,
            'bairro': self.bairro,
            'cep': self.cep,
            'cidade_id': self.cidade_id
        }

class EnderecoInsert(BaseModel, AbstractModel):
    logradouro: str
    complemento: str
    bairro: str
    cep: str
    cidade_id: int

    def to_dict(self):
        return {
            'id': self.id,
            'logradouro': self.logradouro,
            'complemento': self.complemento,
            'bairro': self.bairro,
            'cep': self.cep,
            'cidade_id': self.cidade_id
        }