from config.connection import DBConnectionHandler
from models.cidade_model import Cidade
from models.endereco_model import Endereco, EnderecoInsert
from models.exception_not_found_model import NotFound

from sqlalchemy.orm.exc import NoResultFound

from models.exception_not_found_model import NotFound

class EnderecoRepository:

    def listAll(self, filtros):
        with DBConnectionHandler() as db:
            try:
                if len(filtros) == 0:
                    data = db.session.query(Endereco).all()
                    return [d.to_dict() for d in data]
                else:
                    consulta = db.session.query(*filtros).select_from(Endereco).all()
                    data = [dict(d) for d in consulta]
                    if len(data) == 0:
                        raise NotFound('Endereços')
                    return [dict(d) for d in consulta]
            except Exception as e:
                db.session.rollback()
                raise e

    def findById(self, id):
        with DBConnectionHandler() as db:
            try:
                data = db.session.query(Endereco).filter(Endereco.id == id).one()
                return data.to_dict()
            except NoResultFound:
                raise NotFound('Endereço')
            except Exception as e:
                db.session.rollback()
                raise e
            
    def findByCidadeId(self, id_cidade):
        with DBConnectionHandler() as db:
            try:
                data = db.session.query(Endereco).join(Cidade).filter(Cidade.id == id_cidade).all()
                if data:
                    return [d.to_dict() for d in data]
                else:
                    raise NotFound('Endereço')
            except Exception as e:
                db.session.rollback()
                raise e

    def insert(self, newEndereco: EnderecoInsert):
        with DBConnectionHandler() as db:
            try:
                db_endereco = Endereco(**newEndereco.__dict__)
                db.session.add(db_endereco)
                db.session.commit()
                return 'Endereço cadastrado com sucesso!'
            except Exception as e:
                db.session.rollback()
                raise e

    def update(self, endereco_id: int, newEndereco: EnderecoInsert):
        with DBConnectionHandler() as db:
            try:
                newEnderecoUpdate = newEndereco.to_dict()
                newEnderecoUpdate['id'] = endereco_id
                enderecoUpdate = db.session.query(Endereco).filter(Endereco.id == endereco_id).first()
                if enderecoUpdate:
                    for key, value in newEnderecoUpdate.items():
                        setattr(enderecoUpdate, key, value)
                    db.session.commit()
                    return enderecoUpdate.to_dict()
            except Exception as e:
                db.session.rollback()
                raise e

    def delete(self, endereco_id: int):
        with DBConnectionHandler() as db:
            try:
                if db.session.query(Endereco).filter(Endereco.id == endereco_id).first():
                    db.session.query(Endereco).filter(Endereco.id == endereco_id).delete()
                    db.session.commit()
                    return 'Endereco deletado com sucesso!'
                else:
                    raise NotFound('Endereço')
            except Exception as e:
                db.session.rollback()
                raise e