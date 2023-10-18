from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from databases import Database
from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table
from sqlalchemy.sql import select

DATABASE_URL = "postgresql://postgres:1234@localhost/api_cep"
database = Database(DATABASE_URL)

app = FastAPI()

@app.on_event("startup")
async def startup_db_client():
    await database.connect()

@app.on_event("shutdown")
async def shutdown_db_client():
    await database.disconnect()

metadata = MetaData()

endereco = Table(
    "endereco",
    metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("logradouro", String),
    Column("complemento", String),
    Column("bairro", String),
    Column("cidade", String),
    Column("uf", String),
    Column("cep", String),
)

class Endereco(BaseModel):
    logradouro: str
    complemento: str
    bairro: str
    cidade: str
    uf: str
    cep: str

@app.get("/enderecos/all", response_model=list[dict])
async def listAll():
    columns = [endereco.c.logradouro, endereco.c.cep]
    query = select(columns)
    enderecos = await database.fetch_all(query)
    result = [dict(resultado) for resultado in enderecos]
    return result

@app.get("/enderecos/{endereco_id}", response_model=dict)
async def findById(endereco_id: int):
    columns = [endereco.c.cep, endereco.c.logradouro]
    query = select(columns).where(endereco.c.id == endereco_id)
    resultado = await database.fetch_one(query)
    if resultado is None:
        raise HTTPException(status_code=404, detail="Endereço não encontrada")
    return dict(resultado)

@app.post("/enderecos/", response_model=Endereco)
async def insert(newEndereco: Endereco):
    query = endereco.insert().values(
        logradouro = newEndereco.logradouro,
        complemento = newEndereco.complemento,
        bairro = newEndereco.bairro,
        cidade = newEndereco.cidade,
        uf = newEndereco.uf,
        cep = newEndereco.cep
    )
    endereco_id = await database.execute(query)
    return {**newEndereco.dict(), "id": endereco_id}

@app.put("/enderecos/{endereco_id}", response_model=Endereco)
async def update(endereco_id: int, newEndereco: Endereco):
    query = (
        endereco
        .update()
        .where(endereco.c.id == endereco_id)
        .values(
            logradouro = newEndereco.logradouro,
            complemento = newEndereco.complemento,
            bairro = newEndereco.bairro,
            cidade = newEndereco.cidade,
            uf = newEndereco.uf,
            cep = newEndereco.cep
        )
    )
    await database.execute(query)
    return {**newEndereco.dict(), "id": endereco_id}

@app.delete("/enderecos/{endereco_id}", response_model=dict)
async def delete(tarefa_id: int):
    query = endereco.delete().where(endereco.c.id == tarefa_id)
    await database.execute(query)
    return {"message": "Tarefa deletada"}