from sqlalchemy import Column, Integer

class AbstractModel:
    __tablename__ = 'abstract_model'
    id = Column(Integer, primary_key=True)