from fastapi import APIRouter, HTTPException

from controllers.endereco_controller import EnderecoController
from models.endereco_model import EnderecoInsert

route = APIRouter()

filtros = []

@route.get("/enderecos/all", response_model=list[dict])
def listAll():
    enderecos = EnderecoController().listAll(filtros)
    return enderecos

@route.get("/enderecos/{endereco_id}", response_model=dict)
def findById(endereco_id: int):
    endereco = EnderecoController().findById(endereco_id)
    if endereco is None:
        raise HTTPException(status_code=404, detail="Endereço não encontrado")
    return endereco

@route.get("/enderecos/cidade/{cidade_id}", response_model=list[dict])
def findByCidadeId(cidade_id: int):
    endereco = EnderecoController().findByCidadeId(cidade_id)
    if endereco is None:
        raise HTTPException(status_code=404, detail="Endereço não encontrado")
    return endereco

@route.post("/enderecos/")
def insert(newEndereco: EnderecoInsert) -> str:
    return EnderecoController().insert(newEndereco)

@route.put("/enderecos/{endereco_id}", response_model=dict)
def update(endereco_id: int, newEndereco: EnderecoInsert):
    return EnderecoController().update(endereco_id, newEndereco)

@route.delete("/enderecos/{endereco_id}", response_model=str)
def delete(endereco_id: int):
    return EnderecoController().delete(endereco_id)