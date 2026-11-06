from repository.contato_repository import ContatoRepository

class ContatoService:
    def __init__(self):
        self.__repository = ContatoRepository()

    def cadastrar(self, contato):
        if contato.nome == "" or contato.telefone == "":
            raise ValueError("O nome e o telefone são obrigatorios.")
        if len(contato.nome) > 100:
            raise ValueError("O nome deve ser no maximo 100 caacteres.")
        if len(contato.telefone) > 20:
            raise ValueError("O telefone deve ter no maximo 20 caracteres.")
        if len(contato.email) > 100:
            raise ValueError("O e-mail deve ter no maximo 100 caracteres.")
        if len(contato.mensagem) > 200:
            raise ValueError("A mensagem deve ter no maximo 200 caracteres.")
        self.__repository.cadastrar(contato)

    def listar(self):
        return self.__repository.listar()

    def get_por_id(self,id):
        if id < 1:
            raise ValueError("O id deve ser igual ou maior que 1.")
        return self.__repository.get_por_id(id)
    
    def alterar(self, contato):
        if contato.id < 1:
            raise ValueError("O id deve ser igual ou maio que 1.")
        if contato.nome == "" or contato.telefone == "":
            raise ValueError("O nome e o telefone são obrigatorios.")
        if len(contato.nome) > 100:
            raise ValueError("O nome deve ser no maximo 100 caacteres.")
        if len(contato.telefone) > 20:
            raise ValueError("O telefone deve ter no maximo 20 caracteres.")
        if len(contato.email) > 100:
            raise ValueError("O e-mail deve ter no maximo 100 caracteres.")
        if len(contato.mensagem) > 200:
            raise ValueError("A mensagem deve ter no maximo 200 caracteres.")
        self.__repository.alterar(contato)

    def excluir(self, id):
        if id < 1:
            raise ValueError("O id deve ser igual ou maio que 1.")
        self.__repository.excluir(id)