from flask import Blueprint, render_template

caracteristicas_flaskSQL_bp = Blueprint("caracteristicas_flaskSQL",__name__)

@caracteristicas_flaskSQL_bp.route("/caracteristicas_flaskSQL")
def caracteristicas_flaskSQL():
    return render_template("caracteristicas_flaskSQL.html")