from flask import Blueprint, render_template

sobre_bp = Blueprint("sobre", __name__)

@sobre_bp.route("/sobre")
def sobre():
    lista = [
        "Desenvolvimento de Aplicações Desktop",
        "Desenvolvimento de Aplicações Web",
        "Desenvolvimento de Aplicações Mobile"
    ]
    exibir = True
    return render_template(
        "sobre.html", 
        lista=lista, 
        exibir=exibir
    )