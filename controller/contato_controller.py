from flask import Blueprint, render_template, request
from service.contato_service import ContatoService
from model.contato import Contato

contato_bp = Blueprint("contato", __name__)

service = ContatoService()

@contato_bp.route("/contato", methods=["GET","POST"])
def contato():
    if request.method == "POST":
        """
        nome = request.form.get("nome")
        telefone = request.form.get("telefone")
        email = request.form.get("email")
        mensagem = request.form.get("mensagem")
        return f"Contatos {nome} - {telefone} - {email} - {mensagem}", 200, {"Content-Type":"text/plain"}
        """
        contato = Contato(**request.form)
        service.cadastrar(contato)
        return render_template("mensagem.html", texto="Contato cadastrado!")
    return render_template("contato.html")

@contato_bp.route("/listagemcontato")
def listar():
    contatos = service.listar()
    return render_template("/listagem_contato.html", contatos=contatos)  

@contato_bp.route("/alterar", methods=["GET", "POST"])
def alterar():
    if request.method == "POST":
        id = int(request.form.get("id"))
        nome = request.form.get("nome")
        telefone = request.form.get("telefone")
        email = request.form.get("email")
        mensagem = request.form.get("mensagem")
        contato = Contato(nome, telefone, email, mensagem)
        contato.id = id
        service.alterar(contato)
        return render_template("mensagem.html", texto="Contato Alterado!")
    # http://localhost:9000/alterar?id=1
    id = int(request.args.get("id"))
    contato = service.get_por_id(id)
    return render_template("alterar_contato.html", contato=contato)

@contato_bp.route("/excluir")
def excluir():
    id = int(request.args.get("id"))
    service.excluir(id)
    return render_template("mensagem.html", texto="Contato excluido!")