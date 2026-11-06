from database import Session
from model.contato import Contato

class ContatoRepository:
    def __init__(self):
        self.__session = Session()

    def cadastrar(self, contato):
        self.__session.add(contato)
        self.__session.commit()
        self.__session.close()

    def listar(self):
        contatos = self.__session.query(Contato).all()
        self.__session.close()
        return contatos

    def get_por_id(self, id):
        contato = self.__session.get(Contato,id)
        self.__session.close()
        return contato

    def alterar(self, contato):
        contato_alterar = self.__session.get(Contato, contato.id)
        if contato_alterar:
            contato_alterar.nome = contato.nome
            contato_alterar.telefone = contato.telefone
            contato_alterar.email = contato.email
            contato_alterar.mensagem = contato.mensagem
            self.__session.commit()
            self.__session.refresh(contato_alterar)
        self.__session.close()

    def excluir(self,id):
        contato = self.__session.get(Contato, id)
        if contato:
            self.__session.delete(contato)
            self.__session.commit()
        self.__session.close()