from sqlalchemy import Column, Integer, String
from database import Base

class Contato(Base):
    __tablename__ = "contato"
    id = Column(Integer, autoincrement=True, primary_key=True)
    nome = Column(String(100), nullable=False)
    telefone = Column(String(20), nullable=False)
    email = Column(String(100))
    mensagem = Column(String(200))

    def __init__(self, nome:str,telefone:str,email:str,mensagem:str):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.mensagem = mensagem