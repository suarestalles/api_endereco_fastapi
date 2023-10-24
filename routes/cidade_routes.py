from fastapi import APIRouter, HTTPException

from controllers.cidade_controller import CidadeController
from models.cidade_model import Cidade, CidadeInsert

route = APIRouter()

filtros = []

@route.get("/cidades/all", response_model=list[dict])
def listAll():
    cidades = CidadeController().listAll(filtros)
    return cidades

@route.get("/cidades/{cidade_id}", response_model=dict)
def findById(cidade_id: int):
    cidade = CidadeController().findById(cidade_id)
    if cidade is None:
        raise HTTPException(status_code=404, detail="Cidade não encontrada")
    return cidade

@route.post("/cidades/")
def insert(newCidade: CidadeInsert) -> str:
    return CidadeController().insert(newCidade)

@route.put("/cidades/{cidade_id}", response_model=dict)
def update(cidade_id: int, newCidade: CidadeInsert):
    return CidadeController().update(cidade_id, newCidade)

@route.delete("/cidades/{cidade_id}", response_model=str)
def delete(cidade_id: int):
    return CidadeController().delete(cidade_id)