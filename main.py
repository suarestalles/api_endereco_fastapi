# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel

# from databases import Database
# from databases import Database
# from sqlalchemy import Column, Integer, String, MetaData, Table
# from sqlalchemy.sql import select
# from sqlalchemy.orm import sessionmaker

# app = FastAPI()

# DATABASE_URL = "postgresql://postgres:1234@localhost/api_cep"
# database = Database(DATABASE_URL)

# @app.on_event("startup")
# async def startup_db_client():
#     await database.connect()

# @app.on_event("shutdown")
# async def shutdown_db_client():
#     await database.disconnect()



# class Cidade(BaseModel):
#     nome: str

# class Endereco(BaseModel):
#     logradouro: str
#     complemento: str
#     bairro: str
#     cidade_id: int
#     uf: str
#     cep: str

# @app.get("/enderecos/all", response_model=list[dict])
# async def listAll():
#     columns = [endereco.c.logradouro, endereco.c.cep]
#     query = select(columns)
#     enderecos = await database.fetch_all(query)
#     result = [dict(resultado) for resultado in enderecos]
#     return result

# @app.get("/enderecos/{endereco_id}", response_model=dict)
# async def findById(endereco_id: int):
#     columns = [endereco.c.id, endereco.c.cep]
#     query = select(columns).where(endereco.c.id == endereco_id)
#     resultado = await database.fetch_one(query)
#     if resultado is None:
#         raise HTTPException(status_code=404, detail="Endereço não encontrada")
#     return dict(resultado)

# @app.post("/enderecos/", response_model=Endereco)
# async def insert(newEndereco: Endereco):
#     query = endereco.insert().values(
#         logradouro = newEndereco.logradouro,
#         complemento = newEndereco.complemento,
#         bairro = newEndereco.bairro,
#         cidade = newEndereco.cidade,
#         uf = newEndereco.uf,
#         cep = newEndereco.cep
#     )
#     endereco_id = await database.execute(query)
#     return {**newEndereco.dict(), "id": endereco_id}

# @app.put("/enderecos/{endereco_id}", response_model=Endereco)
# async def update(endereco_id: int, newEndereco: Endereco):
#     query = (
#         endereco
#         .update()
#         .where(endereco.c.id == endereco_id)
#         .values(
#             logradouro = newEndereco.logradouro,
#             complemento = newEndereco.complemento,
#             bairro = newEndereco.bairro,
#             cidade = newEndereco.cidade,
#             uf = newEndereco.uf,
#             cep = newEndereco.cep
#         )
#     )
#     await database.execute(query)
#     return {**newEndereco.dict(), "id": endereco_id}

# @app.delete("/enderecos/{endereco_id}", response_model=dict)
# async def delete(tarefa_id: int):
#     query = endereco.delete().where(endereco.c.id == tarefa_id)
#     await database.execute(query)
#     return {"message": "Tarefa deletada"}

#--------------------------------------------------------------------------------------------------------------------

# from fastapi import FastAPI
# from sqlalchemy import Column, String, Integer, create_engine, Table
# from sqlalchemy.orm import declarative_base, sessionmaker, relationship
# from sqlalchemy import ForeignKey

# from models.abstract_model import AbstractModel

# app = FastAPI()

# engine = create_engine('postgresql://postgres:1234@localhost/api_cep', echo=True)

# Base = declarative_base()

# class Cidade(Base, AbstractModel):
#     __tablename__ = 'cidade'
#     nome = Column(String)
#     uf = Column(String)

# class Endereco(Base, AbstractModel):
#     __tablename__ = 'endereco'
#     cidade_id = Column(Integer, ForeignKey('cidade.id'))
#     logradouro = Column(String)
#     complemento = Column(String)
#     bairro = Column(String)
#     cep = Column(String)

# Base.metadata.create_all(engine)
# conexao = sessionmaker(bind=engine)
# c = conexao()

# cidadeEnd = Cidade(
#     nome = 'Mineiros',
#     uf = 'GO',
# )

# c.add(cidadeEnd)
# c.commit()

# testeId = c.query(Cidade.nome).filter_by(id = 3)
# resul = testeId.scalar()
# print(resul)

# endereco = Endereco(
#     logradouro = 'Av. das Laranjeiras',
#     complemento = 'Casa 1758',
#     bairro = 'Centro',
#     cidade_id = resul,
#     uf = 'GO',
#     cep = '79461214'
# )

# c.add(endereco)
# c.commit()

# query_enderecos = c.query(Endereco, Cidade).join(Endereco, Cidade.id == Endereco.cidade_id).with_entities(Endereco.cep, Cidade.nome).filter_by(id = 31)
# for e in query_enderecos :
#     print(e)

#--------------------------------------------------------------------------------------------------------------------
from fastapi import FastAPI
from config.exception_handler import not_found_exception_handler
from models.exception_not_found_model import NotFound
from routes import endereco_routes, cidade_routes

app = FastAPI()

app.include_router(endereco_routes.route)
app.include_router(cidade_routes.route)
app.add_exception_handler(NotFound, not_found_exception_handler)