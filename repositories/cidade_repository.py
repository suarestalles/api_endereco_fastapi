from config.connection import DBConnectionHandler
from models.cidade_model import Cidade, CidadeInsert

from sqlalchemy.orm.exc import NoResultFound

from models.exception_not_found_model import NotFound

class CidadeRepository:

    def listAll(self, filtros):
        with DBConnectionHandler() as db:
            try:
                if len(filtros) == 0:
                    data = db.session.query(Cidade).all()
                    return [d.to_dict() for d in data]
                else:
                    data = db.session.query(*filtros).select_from(Cidade).all()
                    return [dict(d) for d in data]
            except Exception as e:
                db.session.rollback()
                raise e

    def findById(self, id):
        with DBConnectionHandler() as db:
            try:
                data = db.session.query(Cidade).filter(Cidade.id == id).one()
                return data.to_dict()
            except NoResultFound:
                return None
            except Exception as e:
                db.session.rollback()
                raise e

    def insert(self, newCidade: CidadeInsert):
        with DBConnectionHandler() as db:
            try:
                db_cidade = Cidade(**newCidade.__dict__)
                db.session.add(db_cidade)
                db.session.commit()
                return 'Cidade cadastrada com sucesso!'
            except NoResultFound:
                NotFound('Cidade')
            except Exception as e:
                db.session.rollback()
                raise e

    def update(self, cidade_id: int, newCidade: CidadeInsert):
        with DBConnectionHandler() as db:
            try:
                newCidadeUpdate = newCidade.to_dict()
                newCidadeUpdate['id'] = cidade_id
                cidadeUpdate = db.session.query(Cidade).filter(Cidade.id == cidade_id).first()
                if cidadeUpdate:
                    for key, value in newCidadeUpdate.items():
                        setattr(cidadeUpdate, key, value)
                    db.session.commit()
                    return cidadeUpdate.to_dict()
            except Exception as e:
                db.session.rollback()
                raise e

    def delete(self, cidade_id: int):
        with DBConnectionHandler() as db:
            try:
                if db.session.query(Cidade).filter(Cidade.id == cidade_id).first():
                    return 'Não foi possível deletar esta cidade pois existem endereços relacionados. Exclua todos os endereços antes de deletar esta cidade!'
                elif not db.session.query(Cidade).filter(Cidade.id == cidade_id).first():
                    raise NotFound('Cidade')
                else:
                    db.session.query(Cidade).filter(Cidade.id == cidade_id).delete()
                    db.session.commit()
                    return 'Cidade deletada com sucesso!'
            except Exception as e:
                db.session.rollback()
                raise e